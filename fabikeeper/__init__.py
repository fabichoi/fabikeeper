from flask import Flask

db = 'database'


def create_app():
    print('run: create_app()')
    app = Flask(__name__)

    @app.route('/')
    def index():
        return 'welcome to the fabikeeper __init__'

    return app
