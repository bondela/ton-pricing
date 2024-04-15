from icecream import ic
from pydantic import SecretStr, PostgresDsn, RedisDsn, validator, field_validator, ValidationInfo
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    bot_token: SecretStr
    # postgres_dsn: PostgresDsn
    # redis_dsn: RedisDsn

    channel_id: int = -1002068600035

    db_name: str
    db_user: SecretStr
    db_password: SecretStr
    db_host: str
    db_port: int

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


    # @field_validator('postgres_dsn')
    # def validate_postgres_dsn(cls, v: PostgresDsn, info: ValidationInfo) -> PostgresDsn:
    #     if v["postgres_dsn"] and not v:
    #         assert f"{info.field_name} is empty"
    #     return v


config = Settings()
ic(config.model_dump())
