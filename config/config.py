from pydantic import BaseSettings  # type: ignore


class Settings(BaseSettings):
    STAGING_DIRECTORY: str = "data/"
    SUCCESSFUL_INGESTION_DIR: str = "inserted"
    UNSUCCESSFUL_INGESTION_DIR: str = "aborted"
    LOADER_CONNECTION_URI: str = ""
    LOADER_CONNECTION_URI_PROD: str = ""
    EXTRACTION_CONFIG: str = "/src/config/extraction_config.yaml"
    SCRAPPING_CONFIG: str = "/src/config/scrapping_conf.yaml"

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
