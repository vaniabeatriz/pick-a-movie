import requests


class MovieFetcher:
    def __init__(self):
        id = None
        title = None
        poster_url = None
        rating = None

    def fetch_random_movie(self):
        random_id = 123 # usar um metodo para pegar um random int
        self.fetch(random_id)

    def fetch(self, movie_id):
        # chamar a api e colocar em uma variavel
        # movie = results...
        # filtrar os campos que eu quero
        # atribuir aos atributos
        pass

