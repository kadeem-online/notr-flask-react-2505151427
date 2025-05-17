# standard library imports
import os

# Third party imports
from dotenv import load_dotenv
from flask import (Flask)

# local application imports
import backend.extensions as EXTENSIONS
import backend.models as MODELS

# load variables from .env file.
# used override due to local bug parsing ":" as "\x3a" in .env values
load_dotenv(override=True)


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    # boolean to check if FLASK_ENV is development mode
    is_development: bool = os.getenv("FLASK_ENV").lower() == "development"

    # set the configuration settings.
    if test_config is None:
        if is_development:
            # load the development environment.
            app.config.from_object("backend.config.DevelopmentConfig")
        else:
            # otherwise default to the production environment.
            app.config.from_object("backend.config.ProductionConfig")
    else:
        # load the testing configuration, then try to apply any other custom
        # testing configurations.
        app.config.from_object("backend.config.TestingConfig")
        try:
            app.config.from_mapping(test_config)
        except Exception as e:
            print(f"Failed to load test configuration: {e}")

    # ensure the instance folder has been created
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # initialize extensions
    EXTENSIONS.database.init_app(app)
    EXTENSIONS.migrate.init_app(app, EXTENSIONS.database)

    @app.route("/")
    def index():
        return "Hello Flask"

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
