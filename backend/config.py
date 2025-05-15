# standard libray imports
import os


class DefaultConfig():
    """
    The default configuration settings for the Flask application. All other
    configurations should inherit from this as it contains the required
    configurations fields.
    """
    DEBUG: bool = False
    TESTING: bool = False


class DevelopmentConfig(DefaultConfig):
    """
    The development configuration settings.
    """
    DEBUG = True


class ProductionConfig(DefaultConfig):
    """
    The production configuration settings.
    """


class TestingConfig(DefaultConfig):
    """
    The testing configuration settings.
    """
    TESTING = True
