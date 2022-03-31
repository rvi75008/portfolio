import asyncio
import io
import logging
import os
import shutil
from abc import ABC
from datetime import datetime
from typing import Optional

import aiofiles
import pandas as pd
from psycopg2 import DatabaseError, OperationalError
from sqlalchemy import create_engine

from config.config import settings


class Loader(ABC):
    def load(self, data: str, file: str) -> None:
        ...  # pragma: no cover


class InsertionError(Exception):
    pass


class PostgresLoader(Loader):
    def __init__(self, connection_uri: str):
        self.connection_uri = connection_uri
        self.logger = logging.getLogger(__name__)

    def load(self, data: str, file: str) -> None:
        table = file.split("/")[-1].split(".")[0]
        connection = create_engine(self.connection_uri, pool_size=20)
        try:
            pd.read_csv(filepath_or_buffer=io.StringIO(data)).to_sql(
                f"{table}_stg",
                connection,
                if_exists="append",
                index=False,
                method="multi",
            )
        except (OperationalError, DatabaseError) as e:
            self.logger.error(f"Error while inserting data into {table}: {e}")
            raise InsertionError(f"Error while inserting data into {table}: {e}")


class AsyncPostgresLoader(PostgresLoader):
    def __init__(self, connection_params: str):
        super().__init__(connection_params)

    async def async_load(self, file: str) -> None:
        async with aiofiles.open(file, mode="r", buffering=1) as f:
            data = await f.read()
            self.load(data, file)


async def main(input_dir: str, target: Optional[str] = None):
    async_postgres_loader = AsyncPostgresLoader(
        settings.LOADER_CONNECTION_URI
        if target == "dev"
        else settings.LOADER_CONNECTION_URI_PROD
    )
    # List files to insert
    files_to_insert = [f"{input_dir}/{f}" for f in os.listdir(input_dir)]
    success_dir = (
        f"/{target}/{settings.SUCCESSFUL_INGESTION_DIR}"
        if target
        else settings.SUCCESSFUL_INGESTION_DIR
    )
    failure_dir = (
        f"/{target}/{settings.SUCCESSFUL_INGESTION_DIR}"
        if target
        else settings.UNSUCCESSFUL_INGESTION_DIR
    )
    try:
        await asyncio.gather(
            *[async_postgres_loader.async_load(file) for file in files_to_insert]
        )
        [
            shutil.move(
                f,
                f'{success_dir}/{f.split("/")[-1]}_{datetime.now()}',
            )
            for f in files_to_insert
        ]
        async_postgres_loader.logger.info(
            f"Files inserted into db and moved to {success_dir}"
        )
    except (OSError, InsertionError) as e:
        async_postgres_loader.logger.error(f"Error during insertion: {e}")
        [  # pragma: no cover
            shutil.move(
                f,
                f'{failure_dir}/{f.split("/")[-1]}_{datetime.now()}',
            )
            for f in files_to_insert
        ]


def run_loading(target: Optional[str] = "dev") -> None:
    asyncio.run(
        main(f"{target}/{settings.STAGING_DIRECTORY}", target)
        if target
        else main(settings.STAGING_DIRECTORY)
    )  # pragma: no cover


if __name__ == "__main__":
    asyncio.run(main(f"/dev/{settings.STAGING_DIRECTORY}", "dev"))  # pragma: no cover
