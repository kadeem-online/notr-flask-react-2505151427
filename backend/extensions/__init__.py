# third party libraries
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# main sqlalchemy instance
database: SQLAlchemy = SQLAlchemy()

# main flask migrate instance
migrate: Migrate = Migrate()
