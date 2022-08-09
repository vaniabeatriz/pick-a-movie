import requests
import config
import random

api_key = config.api_key
base_url = "https://api.themoviedb.org/3/movie/" #our query will come from the "latest" movie section, this is a live, and continuously updated part of the api
endpoint = f"{base_url}latest?api_key={api_key}"


class api_requests():
    def __init__(self):
        self.query_latest_data["id"]
        response = requests.get(endpoint, timeout=5)

        if response.status_code == 200:
            print("Successful!")
        else:
            print("There was an error")
            raise Exception  # more to do here with exceptions

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


    def query_latest(): # get the latest film uploaded, grab the id, that's all we need
        response = requests.get(endpoint, timeout=5)
        query_latest_data = response.json()
        latest_id = (query_latest_data["id"])
        return(latest_id)


    def randomise(): # use the id we just grabbed, put it as the last number in the range, do a lil random action
        r = int(latest_id)
        random_movie_id = random.randint(1,r)
        return(random_movie_id)


    def query_search(): # now, do an actual movie search, using the random number we just made
        params = {"adult": False}
        endpoint2 = f"{base_url}{random_movie_id}?api_key={api_key}"
        response2 = requests.get(endpoint2, params=params, timeout=5)
        query_latest_data = response2.json()
        return query_latest_data
        print(query_latest_data)


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
""" best way of returning a random film is to pull from latest - this is continously updated and sequentally - meaning the last film will have the highest id number, so we can
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

