import asyncio
from datetime import datetime
from typing import Any, Dict, List

import aiohttp
import yaml
from bs4 import BeautifulSoup

from config.config import settings
from loader.loader import AsyncPostgresLoader


class Scrapper:
    def __init__(
        self,
        scrappings_config: List[Dict[str, Any]],
        col_to_update: str,
        criteria: List[str],
    ) -> None:
        self.scrappings_config = scrappings_config
        self.col_to_update = col_to_update
        self.criteria = criteria

    async def extract_values(self) -> Any:
        return await asyncio.gather(
            *[
                self.extract_value(
                    url=scrapping["url"], scrapping_config=scrapping["config"]
                )
                for scrapping in self.scrappings_config
            ]
        )

    @classmethod
    async def extract_value(
        cls,
        url: str,
        scrapping_config: Dict[str, Any],
    ) -> float:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                soup = BeautifulSoup(await resp.text(), features="html.parser")
                soup = soup.find_all(
                    scrapping_config["tag"], scrapping_config["name_or_id"]
                )[scrapping_config["tag_index"]]
                try:
                    return (
                        float(
                            soup.contents[scrapping_config["content_index"]].split()[-1]
                        )
                        if scrapping_config["split"]
                        else float(
                            soup.contents[scrapping_config["content_index"]].replace(
                                " ", ""
                            )
                        )
                    )
                except ValueError:
                    return (
                        soup.contents[scrapping_config["content_index"]].split()[-1]
                        if scrapping_config["split"]
                        else soup.contents[scrapping_config["content_index"]].replace(
                            " ", ""
                        )
                    )


def prepare_criteria(
    criteria: List[str], to_scrap: List[Dict[str, Any]]
) -> List[Dict[str, Any]]:
    prepared_criteria = []
    for scrap in to_scrap:
        prepared_criterion = {}
        for crit in criteria:
            if crit == "day":
                prepared_criterion["day"] = datetime.now().strftime("%y-%m-%d")
            else:
                prepared_criterion[crit] = scrap[crit]
        prepared_criteria.append(prepared_criterion)
    return prepared_criteria


def run_scrapping() -> None:
    with open(settings.SCRAPPING_CONFIG) as conf:
        scrappings_config = yaml.load(conf.read(), Loader=yaml.FullLoader)
        scrapper = Scrapper(
            scrappings_config=scrappings_config["to_scrap"],
            col_to_update=scrappings_config["col_to_update"],
            criteria=scrappings_config["criteria"],
        )

    result = asyncio.run(scrapper.extract_values())
    loader = AsyncPostgresLoader(settings.LOADER_CONNECTION_URI_PROD)
    loader.update_from_list_of_dicts(
        values_to_update=result,
        table=scrappings_config["table"],
        col_to_update=scrappings_config["col_to_update"],
        criteria=prepare_criteria(
            scrappings_config["criteria"], scrappings_config["to_scrap"]
        ),
    )
