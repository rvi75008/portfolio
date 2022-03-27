from typing import Dict

from pydantic import BaseSettings


class Settings(BaseSettings):
    STAGING_DIRECTORY: str = "data"
    SUCCESSFUL_INGESTION_DIR: str = "ingested"
    UNSUCCESSFUL_INGESTION_DIR: str = "aborted"
    EXTRACTION_CONFIGURATION: Dict[str, str] = {}
    LOADER_CONNECTION_URI: str = ""

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
