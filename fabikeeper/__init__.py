from flask import Flask

db = 'database'


def create_app():
    print('run: create_app()')
    app = Flask(__name__)

    @app.route('/')
    def index():
        app.logger.info('RUN HELLO WORLD')
        return 'welcome to the fabikeeper __init__'

    ''' Routing '''
    from flask import jsonify, redirect, url_for
    from markupsafe import escape

    @app.route('/test/name/<name>')
    def name(name):
        return f'Name is {name}, {escape({type(name)})}'

    @app.route('/test/id/<int:id>')
    def id(id):
        return 'ID: %d' % id

    @app.route('/test/path/<path:subpath>')
    def path(subpath):
        return subpath

    @app.route('/test/json')
    def json():
        return jsonify({'hello': 'world'})

    @app.route('/test/redirect/<path:subpath>')
    def redirect_url(subpath):
        return redirect(subpath)

    @app.route('/test/urlfor/<path:subpath>')
    def urlfor(subpath):
        return redirect(url_for('path', subpath=subpath))

    from flask import g, current_app

    @app.before_first_request
    def before_first_request():
        app.logger.info('BEFORE_FIRST_REQUEST')

    @app.before_request
    def before_request():
        g.test = True
        app.logger.info('BEFORE_REQUEST')

    @app.after_request
    def after_request(response):
        app.logger.info(f'g.test:{g.test}')
        app.logger.info(f'current_app.config:{current_app.config}')
        app.logger.info('AFTER_REQUEST')
        return response

    @app.teardown_request
    def teardown_request(exception):
        app.logger.info('TEARDOWN_REQUEST')

    @app.teardown_appcontext
    def teardown_appcontext(exception):
        app.logger.info('TEARDOWN_CONTEXT')

    from flask import request

    @app.route('/test/method/<id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
    def method_test(id):
        return jsonify({
            'request.args': request.args,
            'request.form': request.form,
            'request.json': request.json,
            'request.method': request.method
        })

    return app
