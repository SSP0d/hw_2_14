from pydantic import BaseSettings


class Settings(BaseSettings):
    sqlalchemy_database_url: str = 'postgresql://postgres:567234@localhost/rest_app'
    secret_key: str = 'secret_key'
    algorithm: str = 'HS256'
    mail_username: str = 'zatokav@meta.ua'
    mail_password: str = 'FcXH64vtNx3fwmf'
    mail_from: str = 'zatokav@meta.ua'
    mail_port: int = '465'
    mail_server: str = 'smtp.meta.ua'
    redis_host: str = 'localhost'
    redis_port: int = 6379

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
