from waitress import serve
from pyramid.config import Configurator
from pyramid.response import Response


if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('index', '/')

        config.add_static_view(name='static', path='static')

        config.include('pyramid_jinja2')

        config.scan('views')
        app = config.make_wsgi_app()

serve(app, host='0.0.0.0', port=6543)