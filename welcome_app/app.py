from waitress import serve
from pyramid.config import Configurator
from pyramid.response import Response

# http:localhost:6543/ -> hello -> hello_world()

if __name__ == '__main__':

    with Configurator()  as config:

        config.add_route('hello', '/') # configuring a route/url's
        config.add_route('login', '/login') 
        config.add_route('greeting', '/greet')
        config.add_route('welcome', '/welcome/{first}/{last}')

        config.scan('views')
        
        # config.add_view(hello_world, route_name='hello')
        # config.add_view(login_view, route_name='login')
        # config.add_view(greeting_view, route_name='greeting')
        # config.add_view(welcome_view, route_name='welcome')

        app = config.make_wsgi_app()

    serve(app, host='0.0.0.0', port=8080)
