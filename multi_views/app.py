from waitress import serve
from pyramid.config import Configurator
from pyramid.response import Response

if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('home', '/')
        config.add_route('hello', '/howdy')
        config.add_route('redirect', '/goto')
        config.add_route('exception', '/problem')
        config.add_route('welcome', '/welcome/{first}/{last}')
        config.scan('views')
        app = config.make_wsgi_app()
    serve(app, host='0.0.0.0', port=6543)
