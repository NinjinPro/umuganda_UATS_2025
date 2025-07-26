# from pathlib import Path
import os
from dotenv import load_dotenv

# env_path = Path(__file__).resolve().parent.parent.parent / ".env"
# load_dotenv(dotenv_path=env_path)

load_dotenv() # load environment variables

class Config_dev:
    SECRET_KEY = os.environ.get("SECRET_KEY", "uats_admin")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///uats.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", "my-jwt-secret-key")
    SECURITY_PASSWORD_SALT = os.getenv("SECURITY_PASSWORD_SALT", "emailing_192032_password_3891394_salt")


class Config_mail:
    MAIL_SERVER = os.getenv("MAIL_SERVER")
    MAIL_PORT = int(os.getenv("MAIL_PORT"))
    MAIL_USE_TLS = os.getenv("MAIL_USE_TLS", False) == "True"
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
    MAIL_DEFAULT_SENDER = os.getenv("MAIL_DEFAULT_SENDER")

class Config_mail_serializer:
    SECRET_KEY = os.environ.get("SERIALIZER_SECRET_KEY", "uats_admin")
