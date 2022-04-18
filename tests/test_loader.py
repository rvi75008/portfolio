import os
from typing import Any
from unittest.mock import MagicMock

import docker as docker
import pandas as pd
import psycopg2
import pytest as pytest
from freezegun import freeze_time
from pandas import DataFrame
from psycopg2 import OperationalError
from pytest_mock import MockFixture
from sqlalchemy import create_engine

from config import config
from loader.loader import (
    AsyncPostgresLoader,
    InsertionError,
    NoFilesFoundException,
    delete_failed_extraction,
    main,
)


@pytest.fixture(autouse=False)
def io_mocks(mocker: MockFixture) -> None:
    mocker.patch("loader.loader.os.listdir", return_value=["fake_file.csv"])
    mocker.patch("loader.loader.shutil.move")
    current_dir = os.getcwd()
    with open(f"{current_dir}/fake_file.csv", "w") as f:
        f.write("bar,foo\n2, 1\n")


@pytest.fixture(scope="module")
def postgres_server(service_container) -> docker.DockerClient:
    def check(host_port):
        conn = psycopg2.connect(
            host="127.0.0.1",
            port=host_port,
            database="postgres_db",
            user="ubuntu",
            password="passwordpassword",
        )
        cur = conn.cursor()
        cur.execute("SELECT 1;")
        cur.close()
        conn.close()

    return service_container("postgres", check, psycopg2.Error)


@pytest.mark.asyncio
async def test_loader(
    postgres_server: docker.DockerClient,
    io_mocks: MockFixture,
) -> None:
    connection_string = f'postgresql+psycopg2://ubuntu:passwordpassword@localhost:{postgres_server["port"]}/postgres_db'
    config.settings.LOADER_CONNECTION_URI = connection_string
    config.settings.LOADER_CONNECTION_URI_PROD = connection_string
    await main("", "fake_file#bla.csv")
    assert pd.read_sql(
        'select * from "fake_file.csv_stg";', create_engine(connection_string)
    ).to_dict() == {"bar": {0: 2}, "foo": {0: 1}}


@pytest.mark.asyncio
async def test_loader_error(
    mocker: MockFixture, postgres_server: docker.DockerClient, io_mocks: MockFixture
) -> None:
    mocker.patch("loader.loader.pd.DataFrame.to_sql", side_effect=OperationalError)
    mocklogger = MagicMock()
    mocker.patch("loader.loader.logging.getLogger", return_value=mocklogger)
    await main("", "tests")
    assert mocklogger.error.call_count == 2


@pytest.mark.asyncio
async def test_loader_no_file_to_load(mocker: MockFixture) -> None:
    mocker.patch("loader.loader.os.listdir", return_value=[])
    with pytest.raises(NoFilesFoundException):
        await main("./", "development")


def test_load_from_dataframe(mocker: MockFixture) -> None:
    mocked_connection = mocker.MagicMock(name="foo")
    mocker.patch("loader.loader.create_engine", return_value=mocked_connection)

    spy_df = mocker.spy(DataFrame, "to_sql")
    loader = AsyncPostgresLoader("postgresql+psycopg2://foo:bar")
    loader.load_from_dataframe(
        dataframe=pd.DataFrame({"foo": [1, 2, 3], "bar": [3, 1, 4]})
    )
    spy_df.assert_called()


def test_load_from_dataframe_error(mocker: MockFixture) -> None:
    mocked_connection = mocker.MagicMock(name="foo")

    def raise_error(_: Any) -> None:
        raise OperationalError

    mocker.patch("loader.loader.pd.DataFrame.to_sql", side_effect=OperationalError)
    mocked_connection.execute = raise_error
    mocker.patch("loader.loader.create_engine", return_value=mocked_connection)
    loader = AsyncPostgresLoader("postgresql+psycopg2://foo:bar")
    with pytest.raises(InsertionError):
        loader.load_from_dataframe(
            dataframe=pd.DataFrame({"foo": [1, 2, 3], "bar": [3, 1, 4]})
        )


@freeze_time("2022-01-01")
def test_delete_failed_extraction(mocker: MockFixture) -> None:
    mocked_connection = mocker.MagicMock(name="foo")
    mocker.patch("loader.loader.create_engine", return_value=mocked_connection)
    delete_failed_extraction()
    assert (
        mocked_connection.execute.call_args_list[0][0][0]
        == """delete from details_stg where day='22-01-01'
        and date = (select max(date) from details_stg where day='22-01-01');"""
    )


@freeze_time("2022-01-01")
def test_delete_failed_extraction_error(mocker: MockFixture) -> None:
    mocker.patch("loader.loader.create_engine", side_effect=OperationalError)
    with pytest.raises(InsertionError):
        delete_failed_extraction()
