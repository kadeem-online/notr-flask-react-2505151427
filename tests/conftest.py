# third party imports
import pytest

# local application imports
from backend import create_app
from backend.extensions import database


@pytest.fixture
def app():
    app = create_app("testing")
    with app.app_context():
        database.create_all()
        yield app
        database.session.remove()
        database.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()
