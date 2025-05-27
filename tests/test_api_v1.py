import pytest


class TestApiV1():
    """
    Class for testing API V1
    """

    def test_connection(self, client):
        """
        Tests connection to API v1 by prompting the base endpoint of the api.
        """

        response = client.get("/api/v1/")
        assert response.status_code == 200

        data = response.get_json()
        assert data is not None

        expected_message = "API v1 is running"
        assert data.get("message") == expected_message


class TestAuthRoutes():
    """
    Class for testing Auth routes.
    """

    @pytest.fixture(autouse=True)
    def setup_method(self, client):
        """
        Setup method to initialize any required resources before each test.
        """
        # setup endpoint urls for the auth routes.
        self.registration_endpoint: str = "/api/v1/auth/register"

        # set the default user details.
        self.default_email: str = "default_user@tests.com"
        self.default_password: str = "default_password"

        # Register the default user.
        client.post(
            self.registration_endpoint,
            json={
                "email": self.default_email,
                "password": self.default_password,
                "confirm_password": self.default_password,
            }
        )

    def test_register(self, client):
        """
        Tests registering a new user
        """

        response = client.post(
            self.registration_endpoint,
            json={
                "email": "test_user@tests.com",
                "password": "test_password",
                "confirm_password": "test_password",
            }
        )

        assert response.status_code == 201

    def test_register_existing_user(self, client):
        """
        Tests registering using an email which is already registered.
        """

        #  try registering the default user again.
        response = client.post(
            self.registration_endpoint,
            json={
                "email": self.default_email,
                "password": self.default_password,
                "confirm_password": self.default_password
            }
        )

        assert response.status_code == 400

    def test_register_missing_fields(self, client):
        """
        Test registering a user with missing fields.
        """
        email: str = "test_user@tests.com"
        password: str = "test_password"

        # try registering without an email addresss.
        missing_email_response = client.post(
            self.registration_endpoint,
            json={
                "password": password,
                "confirm_password": password
            }
        )

        assert missing_email_response.status_code == 400
        assert "Missing field: email" in missing_email_response.get_json().get("errors")

        # try registering without a password.
        missing_password_response = client.post(
            self.registration_endpoint,
            json={
                "email": email,
                "confirm_password": password
            }
        )

        assert missing_password_response.status_code == 400
        assert "Missing field: password" in missing_password_response.get_json().get("errors")

        # try registering without a confrim password.
        missing_confirm_password_response = client.post(
            self.registration_endpoint,
            json={
                "email": email,
                "password": password
            }
        )

        assert missing_confirm_password_response.status_code == 400
        assert "Missing field: confirm_password" in missing_confirm_password_response.get_json().get("errors")

    def test_register_password_mismatch(self, client):
        """
        Tests mismatching passwords during registration.
        """

        response = client.post(
            self.registration_endpoint,
            json={
                "email": "test_user@tests.com",
                "password": "test_password",
                "confirm_password": "different_password"
            }
        )

        assert response.status_code == 400
        assert "Password does not match confirm password." in response.get_json().get("errors")

    def test_register_short_password(self, client):
        """
        Tests registering a user with a short password.
        """

        response = client.post(
            self.registration_endpoint,
            json={
                "email": "test_user@tests.com",
                "password": "short",
                "confirm_password": "short"
            }
        )

        assert response.status_code == 400
        assert "Password is too short." == response.get_json().get("message")

    def test_register_invalid_email(self, client):
        """
        Test registering the user with an invalid email address.
        """

        # TODO: Add test with an invalid email address.
