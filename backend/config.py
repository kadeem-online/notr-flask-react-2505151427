# standard libray imports
import os


class DefaultConfig():
    """
    The default configuration settings for the Flask application. All other
    configurations should inherit from this as it contains the required
    configurations fields.
    """
    # basic configuration
    DEBUG: bool = False
    TESTING: bool = False
    SECRET_KEY: str = "notr_secret_key"

    # database configuration
    SQLALCHEMY_DATABASE_URI: str = "sqlite:///notr_database.db"


class DevelopmentConfig(DefaultConfig):
    """
    The development configuration settings.
    """
    # basic configuration
    DEBUG = True
    SECRET_KEY = os.getenv("SECRET_KEY", "dev_secret_key")

    # database configuration
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URI", "sqlite:///notr_dev_databse.db"
    )


class ProductionConfig(DefaultConfig):
    """
    The production configuration settings.
    """
    # basic configuration
    SECRET_KEY = os.getenv("SECRET_KEY", "prod_secret_key")

    # database configuration
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URI", "sqlite:///notr_dev_databse.db"
    )


class TestingConfig(DefaultConfig):
    """
    The testing configuration settings.
    """
    # basic configuration
    TESTING = True
