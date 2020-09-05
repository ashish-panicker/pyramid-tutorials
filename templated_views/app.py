from waitress import serve
from pyramid.config import Configurator
from pyramid.response import Response

if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('hello', '/hello/{name}')
        
        '''route that retuns JSON output'''
        config.add_route('hello_json', '/hello.json')

        config.add_static_view(name='static', path='static')

        '''Add jinja2 templaing engine'''
        config.include('pyramid_jinja2')

        config.scan('views')
        app = config.make_wsgi_app()
    serve(app, host='0.0.0.0', port=6543)
