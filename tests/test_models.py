# third party imports
import pytest
from sqlalchemy import (select, delete)
from sqlalchemy.exc import IntegrityError

# local application imports
from backend.models import (User)
from backend.extensions import database


class TestUser():
    """
    Collection of tests for the user model.
    """

    @pytest.fixture(autouse=True)
    def setUp(self, app):
        # setup the flask app instance
        self.app = app

        # create default user
        self.default_user = User(
            email="tester@tests.com",
            password="pass123"
        )

        with self.app.app_context():
            database.session.add(self.default_user)
            database.session.commit()

    def test_default_user(self):
        """
        Test that the default user is created suring the setup.
        """

        with self.app.app_context():
            stmt = select(User).where(
                User.email == "tester@tests.com"
            )
            user = database.session.execute(stmt).scalars().first()

            assert user is not None
            assert user.password == "pass123"

    def test_user_creation(self):
        """
        Test the creation of a new user.
        """

        new_user = User(
            email="tester2@tests.com",
            password="pass123"
        )

        with self.app.app_context():
            database.session.add(new_user)
            database.session.commit()

            assert new_user.id is not None

    def test_duplicate_user_email(self):
        """
        Test that dupllicate user emails are not allowed.
        """

        duplicate_user = User(
            email="tester@tests.com",
            password="pass123"
        )

        with self.app.app_context():
            database.session.add(duplicate_user)

            with pytest.raises(IntegrityError):
                database.session.commit()

    def test_user_deletion(self):
        """
        Test the deletion of a user.
        """
        # holds the test user email to avoid hardcodding
        default_email = "tester@tests.com"

        # delete the default user
        with self.app.app_context():
            # get the default user to ensure he exists.
            fetch_stmt = select(User).where(
                User.email == "tester@tests.com"
            )
            user = database.session.execute(fetch_stmt).scalars().first()
            assert user is not None

            # delete the default user
            database.session.delete(user)
            database.session.commit()

            # ensure that user has and ID of 1
            assert user.id == 1

            # check if the default user record still exists.
            deleted_user = database.session.get(User, user.id)
            assert deleted_user is None
