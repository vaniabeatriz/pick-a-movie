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
