from icecream import ic
from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    bot_token: SecretStr

    channel_id: int = -1002068600035

    db_name: str
    db_user: SecretStr
    db_password: SecretStr
    db_host: str
    db_port: int

    model_config = SettingsConfigDict(env_file="../.env", env_file_encoding="utf-8")


config = Settings()
# ic(config.model_dump())
