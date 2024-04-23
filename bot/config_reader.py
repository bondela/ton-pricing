from typing import Union

from icecream import ic
from pydantic import SecretStr, PostgresDsn, RedisDsn, validator, field_validator, ValidationInfo
from pydantic_settings import BaseSettings, SettingsConfigDict



class Settings(BaseSettings):
    # Unique token for your bot
    bot_token: SecretStr = None

    # Connection URL to postgresql
    postgres_dsn: PostgresDsn

    # Connection URL to redis
    redis_dsn: RedisDsn

    # Channel for publishing exchange rates
    channel_id: int = -1002068600035

    @field_validator('channel_id')
    def validate_bot_token(cls, v: Union[int, str], info: ValidationInfo) -> int:
        if not isinstance(v, int):
            raise Exception(f"{info.field_name} must be integer")
        if not "-" in str(v):
            raise Exception(f"{info.field_name} must contains minus symbol")
        return v

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

config = Settings()
ic(config.model_dump())
