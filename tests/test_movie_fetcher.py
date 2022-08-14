import unittest
from src.api import MovieFetcher


class TestMovieFetcher(unittest.TestCase):
    def setUp(self):
        self.movie = MovieFetcher()

    def test_get_poster_url(self):
        result = self.movie.get_poster_url("a")
        self.assertEqual("https://image.tmdb.org/t/p/w500/a", result)

    def test_get_poster_url_empty(self):
        result = self.movie.get_poster_url(None)
        self.assertEqual("https://www.prokerala.com/movies/assets/img/no-poster-available.webp", result)

    def test_as_json(self):
        self.movie.movie_dict = {'id': 123, 'title': 'Amelie Poulain', 'poster_path': 'amelie.jpg'}
        result = self.movie.as_json()
        expected = {
            'title': 'Amelie Poulain',
            'poster_url': 'https://image.tmdb.org/t/p/w500/amelie.jpg',
            'movie_link': 'http://www.themoviedb.org/movie/123'
        }
        self.assertEqual(expected, result)

    def test_type_latest_id(self):
        result = self.movie.latest_id()
        message = "the latest_id variable is not an int type"
        self.assertIs(type(result), int, message)

    def test_type_random_movie_id(self):
        result = self.movie.random_movie_id()
        message = "the random_movie_id variable is not an int type"
        self.assertIs(type(result), int, message)

    def test_type_movie_dict(self):
        result = self.movie.movie_dict
        message = "the movie_dict variable is not a dict type"
        self.assertIs(type(result), dict, message)


if __name__ == '__main__':
    unittest.main()
