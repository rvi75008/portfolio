from typing import Any

import pytest
from aioresponses import aioresponses
from freezegun import freeze_time
from psycopg2 import OperationalError
from pytest_mock import MockFixture

from loader.loader import InsertionError
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
    mocked_connection = mocker.MagicMock(name="foo")
    mocker.patch("loader.loader.create_engine", return_value=mocked_connection)
    with aioresponses() as m:
        m.get(
            "https://vieux-clous.fr",
            status=200,
            body="""<html><span class="prix">10</span></html>""",
        )
        run_scrapping()
    assert (
        mocked_connection.execute.call_args_list[0][0][0]
        == """UPDATE details SET pu = 10.0 WHERE actif = 'clou' AND day = '22-01-01';"""
    )
    mocker.patch(
        "scrapper.scrapper.yaml.load",
        return_value={
            "table": "details",
            "col_to_update": "actif",
            "criteria": ["actif", "day"],
            "to_scrap": [
                {
                    "actif": "clou",
                    "url": "https://vieux-clous.fr",
                    "config": {
                        "tag": "span",
                        "name_or_id": "name",
                        "content_index": 0,
                        "tag_index": 0,
                        "split": False,
                    },
                }
            ],
        },
    )
    with aioresponses() as m:
        m.get(
            "https://vieux-clous.fr",
            status=200,
            body="""<html><span class="name">fooo</span></html>""",
        )
        run_scrapping()
    assert (
        mocked_connection.execute.call_args_list[1][0][0]
        == """UPDATE details SET actif = 'fooo' WHERE actif = 'clou' AND day = '22-01-01';"""
    )
    mocker.patch(
        "scrapper.scrapper.yaml.load",
        return_value={
            "table": "details",
            "col_to_update": "actif",
            "criteria": ["actif", "price"],
            "to_scrap": [
                {
                    "actif": "clou",
                    "price": 10,
                    "url": "https://vieux-clous.fr",
                    "config": {
                        "tag": "span",
                        "name_or_id": "name",
                        "content_index": 0,
                        "tag_index": 0,
                        "split": False,
                    },
                }
            ],
        },
    )
    with aioresponses() as m:
        m.get(
            "https://vieux-clous.fr",
            status=200,
            body="""<html><span class="name">fooo</span></html>""",
        )
        run_scrapping()
    assert (
        mocked_connection.execute.call_args_list[2][0][0]
        == """UPDATE details SET actif = 'fooo' WHERE actif = 'clou' AND price = 10;"""
    )


def test_run_scrapping_error(mocker: MockFixture) -> None:
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
    mocked_connection = mocker.MagicMock(name="foo")

    def raise_error(_: Any) -> None:
        raise OperationalError

    mocked_connection.execute = raise_error
    mocker.patch("loader.loader.create_engine", return_value=mocked_connection)

    with aioresponses() as m:
        m.get(
            "https://vieux-clous.fr",
            status=200,
            body="""<html><span class="prix">10</span></html>""",
        )
        with pytest.raises(InsertionError):
            run_scrapping()
