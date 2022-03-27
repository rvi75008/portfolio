import asyncio
import io
from typing import Dict, List, Optional

import httpx
import pandas as pd

from config.config import settings
from connectors.helpers.extraction_helpers import clean_df
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

    async def extract_data(self, prefix: str, decimal: Optional[str]) -> None:
        extracted_dataframes = await self.async_extract_csvs(decimal=decimal)
        [
            clean_df(extracted_dataframe, datasource.transformation_logic).to_csv(
                f"{prefix}{datasource.sheet}.csv", index=False
            )
            for extracted_dataframe, datasource in zip(
                extracted_dataframes, self.datasources
            )
        ]


async def main() -> None:
    datasources = [
        DataSource(
            settings.EXTRACTION_CONFIGURATION["spreadsheet_id"],
            sheet,
            transformations[sheet],
        )
        for sheet in settings.EXTRACTION_CONFIGURATION["sheet_names"]
    ]
    connector = Connector(datasources=datasources)
    await connector.extract_data(settings.STAGING_DIRECTORY, ",")


def run_extraction() -> None:
    asyncio.run(main())  # pragma: no cover


if __name__ == "__main__":
    asyncio.run(main())  # pragma: no cover
