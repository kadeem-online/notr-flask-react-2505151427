
# Third party imports
from dotenv import load_dotenv
from flask import (Flask, redirect)


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    @app.route("/")
    def index():
        return "Hello Flask"

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
