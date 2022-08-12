from flask import Flask, render_template
from src.api import MovieFetcher

app = Flask(__name__)


# Creates the pages of the website
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/movie_result/')
def movie_result():
    movie = MovieFetcher()
    movie.fetch_movie()
    movie_json = movie.as_json()
    return render_template('movie_result.html', movie=movie_json)


@app.errorhandler(404)  # This decorator handles a HTTP response error when a page is not found.
def page_not_found(_e):
    return render_template('404.html'), 404


@app.errorhandler(500)  # This decorator handles a HTTP response error when an internal server is raised.
def internal_error(_e):
    # The decorator above requires this function to accept a parameter (e),
    # as we are not using it, we can prefix it with _ (_e) (found this on the internet)
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)
