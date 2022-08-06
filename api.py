import requests
import json
import config


api_key = config.api_key
base_url = "https://api.themoviedb.org/3/movie/latest" #our query will come from the "latest" movie section, this is a live, and continuously updated part of the api
endpoint = f"{base_url}?api_key={api_key}"

#params = {"adult":False,"id":[random_film],"original_title":title,"poster_path":}


#[genre] optional addition


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


r = requests.get(endpoint, timeout=5) #params
data = r.json()
data.keys()

print(data["title"])  #  Instead of print, we need to send this over to the html
print(data["poster_path"])  #  text below from api documentation
# In order to generate a fully working image URL, you'll need 3 pieces of data. Those pieces are a base_url, a file_size and a file_path.
# The first two pieces can be retrieved by calling the  API and the third is the file path you're wishing to grab on a particular media object.


"""parameters (that are useful to us, many more available)
adult               boolean         optional  #  include porn (set to False, obvs lol)
genres              array[object]   optional  #  possible integration
 -name              string          optional  #  genre name
poster_path         string or null  optional  #  gives a /end of url of poster img file
video               boolean         optional  #  gives a video (if available)  """


"""def movie(self, **kwargs):  #  make cody better, put into functions!
     Returns:
path = self._get_path('movie')
response = self._GET(path, kwargs)
self._set_attrs_to_values(response)
return response"""
