# third party imports
from flask_migrate import upgrade


def test_migrations(app):
    """
    Check if applying migrations works.
    """
    with app.app_context():
        upgrade()
