import requests
import config
import random


class MovieFetcher:
    api_key = config.api_key
    base_url = "https://api.themoviedb.org/3/movie/"  # our query will come from the "latest" movie section, this is a live, and continuously updated part of the api
    latest_endpoint = f"{base_url}latest?api_key={api_key}"
    base_file_url = "https://image.tmdb.org/t/p/w500/"
    no_poster_url = "https://www.prokerala.com/movies/assets/img/no-poster-available.webp"

    def __init__(self):
        self.movie_dict = {}

        # try:
        #     response = requests.get('url', timeout=5)
        #     response.raise_for_status()
        #     # Code here will only run if the request is successful
        # except requests.exceptions.HTTPError as errh:
        #     print(errh)
        # except requests.exceptions.ConnectionError as errc:
        #     print(errc)
        # except requests.exceptions.Timeout as errt:
        #     print(errt)
        # except requests.exceptions.RequestException as err:
        #     print(err)

    def latest_id(self):  # get the latest film uploaded, grab the id, that's all we need
        response = requests.get(self.latest_endpoint, timeout=5)
        if response.status_code == 200:
            print("Successful!")
        else:
            print(f"Sorry! There was an error")
            raise Exception
        query_latest_data = response.json()
        latest_id = query_latest_data["id"]
        return int(latest_id)

    def random_movie_id(self): # use the id we just grabbed, put it as the last number in the range, do a lil random action
        last_movie_id = self.latest_id()
        random_movie_id = random.randint(1, last_movie_id)
        return random_movie_id

    def fetch_movie(self):
        # now, do an actual movie get, using the random number we just made
        # in case the request fails or it returns an adult movie it will keep trying with a different random id
        movie_id = self.random_movie_id()
        params = {"adult": False}
        endpoint = f"{self.base_url}{movie_id}?api_key={self.api_key}"
        response = requests.get(endpoint, params=params, timeout=5)
        response_json = response.json()
        if response.status_code != 200 or response_json['adult']:
            print(f"Invalid result. Status code {response.status_code}")
            self.fetch_movie()
        else:
            self.movie_dict = response.json()

    def get_poster_url(self, poster_path):
        if poster_path:
            return f"{self.base_file_url}{poster_path}"
        else:
            return self.no_poster_url

    def get_movie_link(self):  # link to themoviedatabase's own url for picked movie
        movie_link = f"http://www.themoviedb.org/movie/{self.random_movie_id}"
        return movie_link # HB added in PN code please review then delete this comment

    def as_json(self):
        return {
            'title': self.movie_dict['title'],
            'poster_url':  self.get_poster_url(self.movie_dict['poster_path']),
            'movie_link': self.get_movie_link(self.movie_dict['movie_link']), # HB added in this line, not 100% sure correct?
        }


    #def go_again(): # woo boy, that gave us nothing good, lets randomise again!
        # take the exception from query_search and
        # go back to the randomise function with a +1
        # OR
        # go back to randomise entirely different number
        # OPTIONAL EXTRA - store the "bad" number in a file of "no thanks, never again!" (.txt file?)


    # def make_film_data(): # an extra step, turning the film title and poster into usable string to put into html



""" example return from a random movie
{
        "poster_path": "/IfB9hy4JH1eH6HEfIgIGORXi5h.jpg",
        "adult": false,
        "overview": "Jack Reacher must uncover the truth behind a major government conspiracy in order to clear his name. On the run as a fugitive from the law, Reacher uncovers a potential secret from his past that could change his life forever.",
        "release_date": "2016-10-19",
        "genre_ids": [
            53,
            28,
            80,
            18,
            9648
        ],
        "id": 343611,
        "original_title": "Jack Reacher: Never Go Back",
        "original_language": "en",
        "title": "Jack Reacher: Never Go Back",
        "backdrop_path": "/4ynQYtSEuU5hyipcGkfD6ncwtwz.jpg",
        "popularity": 26.818468,
        "vote_count": 201,
        "video": false,
        "vote_average": 4.19
    }"""


#random_film # code for randomising
""" best way of returning a random film is to pull from latest - this is continuously updated and sequentially - meaning the last film will have the highest id number, so we can
1. find out the latest film id
2. use that number to create a range (1 - latest_id)
3. randomise
4. slot random number in our query
5. return query - see if it is a valid link (if not valid, return to start)
6. output film in display - html film with the picture shown
7. lastly, offer a (redo) if user wants to click again for a different film"""

"""Alternatively!
there are 1 - 1000 max pages of films, so randomise in that range, then between 1 -20 (20 per page)"""

#  +1 to the id if our api request doesnt return a valid film - or a poster?


"""below is the easymode - working code from before"""
# response = requests.get(endpoint, timeout=5)
# data = response.json()
# data.keys()

# print(data["id"])
# print(data["title"])
# print(data["poster_path"])
# print(base_image_url + image_data) # make this a string so concat works!


# def format_data(data_from_api):  #  Formats the api output to str for html
# data.format(str("poster_path"))
# return formatted_data

# base_image_url = "https://image.tmdb.org/t/p/original/"
 # image_data = data["poster_path"]
 # converted = json.loads(image_data, parse_float= str)


"""parameters (that are useful to us, many more available)
adult               boolean         optional  #  include porn (set to False, obvs lol)
genres              array[object]   optional  #  possible integration
 -name              string          optional  #  genre name
poster_path         string or null  optional  #  gives a /end of url of poster img file
video               boolean         optional  #  gives a video (if available)  """

