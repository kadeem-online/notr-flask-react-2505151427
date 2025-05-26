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
