# third party imports
from flask import Flask

# local application imports
from backend import create_app


def test_app_exists():
    """
    Test if a flask aplication is created by the app factory.
    """
    app = create_app()
    assert app is not None
    assert isinstance(app, Flask)


def test_app_client_exists():
    """
    Test if the test client is operational.
    """
    app = create_app()
    client = app.test_client()
    response = client.get("/")
    assert response.status_code in (200, 404)


def test_testing_config():
    """
    Check whether the app is run in testing mode when a test_config value is
    passed to the application factory.
    """
    app = create_app("testing")
    assert app.config["TESTING"] is True
