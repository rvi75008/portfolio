from unittest.mock import MagicMock

import docker as docker
import pandas as pd
import psycopg2
import pytest as pytest
from psycopg2 import OperationalError
from pytest_mock import MockFixture
from sqlalchemy import create_engine

from config import config
from loader.loader import main


@pytest.fixture(autouse=True)
def io_mocks(mocker: MockFixture) -> None:
    mocker.patch("loader.loader.os.listdir", return_value=["fake_file.csv"])
    mocker.patch("loader.loader.shutil.move")
    mocker.patch("loader.loader.open")


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
    postgres_server: docker.DockerClient, io_mocks: MockFixture
) -> None:
    connection_string = f'postgresql+psycopg2://ubuntu:passwordpassword@localhost:{postgres_server["port"]}/postgres_db'
    config.settings.LOADER_CONNECTION_URI = connection_string
    await main("tests")
    assert pd.read_sql(
        "select * from fake_file_stg;", create_engine(connection_string)
    ).to_dict() == {"bar": {0: 2}, "foo": {0: 1}}


@pytest.mark.asyncio
async def test_loader_error(
    mocker: MockFixture, postgres_server: docker.DockerClient, io_mocks: MockFixture
) -> None:
    mocker.patch("loader.loader.pd.DataFrame.to_sql", side_effect=OperationalError)
    connection_string = f'postgresql+psycopg2://ubuntu:passwordpassword@localhost:{postgres_server["port"]}/postgres_db'
    mocklogger = MagicMock()
    mocker.patch("loader.loader.logging.getLogger", return_value=mocklogger)
    await main("tests")
    assert mocklogger.error.call_count == 2
