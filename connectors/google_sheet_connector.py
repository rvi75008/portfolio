import asyncio
import datetime
import io
from typing import Dict, List, Optional

import backoff
import httpx
import pandas as pd
import yaml

from config.config import settings
from connectors.helpers.extraction_helpers import (
    ScrapedValuesError,
    prepare_df_for_insertion,
)
from connectors.helpers.transformation_config import transformations  # type: ignore


class DataSource:
    def __init__(
        self,
        spreadsheet_id: str,
        sheet: Optional[str],
        transformation_logic: Optional[Dict],
    ):
        self.spreadsheet_id = spreadsheet_id
        self.sheet = sheet
        self.transformation_logic = transformation_logic

    def build_url(self):
        return f"https://docs.google.com/spreadsheets/d/{self.spreadsheet_id}/gviz/tq?tqx=out:csv&sheet={self.sheet}"


class Connector:
    def __init__(self, datasources: List[DataSource]) -> None:
        self.datasources = datasources

    async def async_extract_csvs(self, decimal: Optional[str]) -> List[pd.DataFrame]:
        dataframes: List[pd.DataFrame] = []
        async with httpx.AsyncClient() as client:
            responses = await asyncio.gather(
                *[client.get(datasource.build_url()) for datasource in self.datasources]
            )
        for response in responses:
            with io.StringIO(response.text) as text_io:
                dataframes.append(pd.read_csv(text_io, decimal=decimal))
        return dataframes

    async def extract_data(
        self, prefix: str, decimal: Optional[str], tries: Optional[int] = 0
    ) -> None:
        try:
            await self.extract_clean_write_file(decimal, prefix)
        except ScrapedValuesError:
            tries += 1
            if tries == 5:
                await self.extract_clean_write_file(
                    decimal, prefix, False
                )  # Write file anyway, we'll have a logic to correct
            else:
                await asyncio.sleep(1.5 * tries)
                await self.extract_data(prefix, decimal, tries)

    async def extract_clean_write_file(self, decimal: str, prefix: str, check: Optional[bool] = True ):
        extracted_dataframes = await self.async_extract_csvs(decimal=decimal)
        [
            prepare_df_for_insertion(
                extracted_dataframe, datasource.sheet, datasource.transformation_logic, check=check
            ).to_csv(
                f"{prefix}{datasource.sheet}#{datetime.datetime.now()}.csv", index=False
            )
            for extracted_dataframe, datasource in zip(
                extracted_dataframes, self.datasources
            )
        ]


async def main(target: Optional[str]) -> None:
    with open(settings.EXTRACTION_CONFIG) as f:
        extraction_config = yaml.load(f, Loader=yaml.FullLoader)[
            target if target else "prod"
        ]
        datasources = [
            DataSource(
                extraction_config["spreadsheet_id"],
                sheet,
                transformations[sheet],
            )
            for sheet in extraction_config["sheet_names"]
        ]
    connector = Connector(datasources=datasources)
    await connector.extract_data(
        f"/{target}/{settings.STAGING_DIRECTORY}"
        if target
        else settings.STAGING_DIRECTORY,
        ",",
    )


def run_extraction(target: Optional[str] = "development") -> None:
    asyncio.run(main(target))  # pragma: no cover


if __name__ == "__main__":
    asyncio.run(main("development"))  # pragma: no cover
