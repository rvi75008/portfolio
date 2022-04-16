from freezegun import freeze_time

from aioresponses import aioresponses
from pytest_mock import MockFixture

from scrapper.scrapper import run_scrapping

@freeze_time("2022-01-01")
def test_run_scrapping(mocker: MockFixture) -> None:
    mocker.patch(
        "scrapper.scrapper.yaml.load",
        return_value={
            "table": "details",
            "col_to_update": "pu",
            "criteria": ["actif", "day"],
            "to_scrap": [
                {
                    "actif": "clou",
                    "url": "https://vieux-clous.fr",
                    "config": {
                        "tag": "span",
                        "name_or_id": "prix",
                        "content_index": 0,
                        "tag_index": 0,
                        "split": False,
                    },
                }
            ],
        },
    )
    mocker.patch("scrapper.scrapper.open")
    mocked_engine = mocker.MagicMock()
    mocked_engine = mocker.patch(
        "loader.loader.create_engine", return_value=mocked_engine
    )
    with aioresponses() as m:
        m.get(
            "https://vieux-clous.fr",
            status=200,
            body="""<html><span class="prix">10</span></html>""",
        )
        run_scrapping()
    assert (
        mocked_engine.mock_execute.call_args_list[0][0]
        == """UPDATE details 
    SET pu = 10 WHERE actif = 'clou' AND day = '22-01-01'; """
    )
