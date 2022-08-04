from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    """Example endpoint returning a random movie
    This is using docstrings for specifications.
    ---
    parameters:
    responses:
      200:
        description: A random movie
        schema:
          type: object
          properties:
            id: int
            title: string
            poster_url: string
            rating: float
    """
    # example
    result = {'id': 1, 'title': 'My Movie', 'poster_url': 'img', 'rating': 4.3}
    return jsonify(result)
