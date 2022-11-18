import requests
import src.config as config
import random
import mysql.connector
import os


class MovieFetcher:
    """
    Class MovieFetcher: returns a random movie from TheMovieDataBase.org api
    
    latest_id:
        determines the latest ID of the last movie, as the database is updated sequentially
    
    random_movie:
        creates a range, using the latest_id, and randomises an int, returning it
        
    fetch_movie:
        creates an endpoint using the random_movie_id, and calls for that movie
        if api returns an empty movie field (movie deleted off database) or an adult film it runs again
    
    get_poster_url:
        creates a img html link from the specific [poster_path] response from the api
        if no poster present (not uploaded on the database) puts an alternative "no image found" img there instead                    
    
    get_movie_link:
        creates a clickable html link to the movie's page on TheMovieDatabase's own site, for more information
    
    as_json:
        creates all the outputs for the relevant links that the html pages will access
    """

    api_key = config.api_key
    base_url = "https://api.themoviedb.org/3/movie/"
    latest_endpoint = f"{base_url}latest?api_key={api_key}"  # Specific endpoint from "latest" section of api
    base_file_url = "https://image.tmdb.org/t/p/w500/"  # base for img file
    no_poster_url = "https://www.prokerala.com/movies/assets/img/no-poster-available.webp"  # alt. if no poster uploaded

    def __init__(self):
        self.movie_dict = {}

    def latest_id(self):  # Querying the latest section of tmdb just to get the last movie uploaded's id
        response = requests.get(self.latest_endpoint, timeout=5)
        if response.status_code == 200:
            print("Successful!")
        else:
            print(f"Sorry! There was an error")
            raise Exception
        query_latest_data = response.json()
        latest_id = query_latest_data["id"]
        return int(latest_id)

    def random_movie_id(self):  # Getting a random int using the range of 1 - the last id we just retrieved
        last_movie_id = self.latest_id()
        random_movie_id = random.randint(1, last_movie_id)
        return random_movie_id

    def fetch_movie(self):  # Fetching the movie from the id we just randomly generated
        #  In case the request fails or it returns an adult movie it will keep trying with a different random id
        movie_id = self.random_movie_id()
        endpoint = f"{self.base_url}{movie_id}?api_key={self.api_key}"
        response = requests.get(endpoint, timeout=5)
        response_json = response.json()
        if response.status_code != 200 or response_json["adult"]:
            print(f"Invalid result. Status code {response.status_code}")
            self.fetch_movie()
        else:
            self.movie_dict = response.json()
            self.log_movie()

    def log_movie(self):
            connection = mysql.connector.connect(
                host=os.getenv('MYSQL_HOST'),
                user=os.getenv('MYSQL_USERNAME'),
                password=os.getenv('MYSQL_PASSWORD'),
                database='pick_a_movie',
            )
            cursor = connection.cursor()
            has_poster = True if self.movie_dict['poster_path'] else False
            movie_id = self.movie_dict['id']
            command = f'INSERT INTO suggested_movies (movie_id, has_poster) VALUES ("{movie_id}", {has_poster})'
            cursor.execute(command)
            connection.commit()
            cursor.close()
            connection.close()

    def get_poster_url(self, poster_path):  # Make img link poster of movie (if poster not available on tmdb, blank pic)
        if poster_path:
            return f"{self.base_file_url}{poster_path}"
        else:
            return self.no_poster_url

    def get_movie_link(self):  # Make a clickable link to tmdb's own page for the movie
        movie_link = f"http://www.themoviedb.org/movie/{self.movie_dict['id']}"
        return movie_link

    def as_json(self):  # Outputs for the movie result html page
        return {
            'title': self.movie_dict['title'],
            'poster_url':  self.get_poster_url(self.movie_dict['poster_path']),
            'movie_link': self.get_movie_link(),
        }
