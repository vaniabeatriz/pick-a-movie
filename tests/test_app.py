import unittest
from src.app import app


class TestApp(unittest.TestCase):
    def __init__(self, methodName):
        super().__init__(methodName=methodName)
        self.client = None

    def setUp(self):
        """ Sets the server up"""
        app.config.update({"TESTING": True})
        self.client = app.test_client()

    def test_home_response(self):
        """It returns a valid response for the Home webpage"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_movie_result_response(self):
        """It returns a valid response for the Movie result webpage"""
        response = self.client.get("/movie_result/")
        self.assertEqual(response.status_code, 200)

    def test_movie_result_old_url_redirect(self):
        """It returns a valid response for the Movie result webpage"""
        response = self.client.get("/movie_result")
        self.assertEqual(response.status_code, 308)

    def test_page_not_found(self):
        """ It returns a page not found response """
        response = self.client.get("/invalid_page")
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
