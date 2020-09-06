from waitress import serve
from pyramid.config import Configurator
from pyramid.response import Response   


def hello_world(request):
    print('URL: ' + request.url)
    name = request.params.get('name', 'No Name Provided')
    url = request.url
    body = '<h1>URL %s with name: %s</h1>' % (url, name)
    return Response(
        content_type="text/html",
        body=body
    )


if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('hello', '/')
        config.add_view(hello_world, route_name='hello')
        app = config.make_wsgi_app()
    serve(app, host='0.0.0.0', port=6543)

#MVC