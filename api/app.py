# app
from flask import Flask,jsonify
from config import Config


def create_app(config=None):
    app = Flask(__name__)
    app.config.from_object(Config)

    @app.route('/')
    def index():
        return  jsonify({"welcome":"Welcome to iReporter"""}),200

    return app

app = create_app()


if __name__ == "__main__":
    app.run()