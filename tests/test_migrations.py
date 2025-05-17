# standard library imports
import tempfile

# third party imports
from flask_migrate import upgrade

# local application imports
from backend import create_app


def test_migrations():
    """
    Check if applying migrations works.
    """
    _, db_path = tempfile.mkstemp(".db")

    app = create_app(test_config={
        "SQLALCHEMY_DATABASE_URI": f"sqlite:///{db_path}"
    })

    with app.app_context():
        upgrade()
