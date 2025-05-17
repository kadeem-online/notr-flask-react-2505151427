# standard library imports
import tempfile

# third party imports
import pytest
from flask_migrate import upgrade

# local application imports
from backend import create_app
from backend.extensions import database


@pytest.fixture
def app():
    """
    Creates the tests application instance.
    """

    # create temporary database file
    db_fd, db_path = tempfile.mkstemp(".db")

    app = create_app(test_config={
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": f"sqlite:///{db_path}",
        "SQLALCHEMY_TRACK_MODIFICATIONS": False
    })
    with app.app_context():
        database.create_all()
        yield app
        database.session.remove()
        database.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()
