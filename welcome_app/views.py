from pyramid.compat import escape
from pyramid.response import Response
from pyramid.view import view_config


@view_config(route_name='hello')
def hello_world(request):
    body = "<h1>Welcome to pyramid web application</h1>"
    print('URL ' + request.url)
    return Response(
        content_type="text/html",
        body=body
    )

@view_config(route_name='login')
def login_view(request):
    body = "<h1>Login view</h1>"
    print('URL ' + request.url)
    return Response(
        content_type="text/html",
        body=body
    )

@view_config(route_name='greeting')
def greeting_view(request):
    
    print('URL ' + request.url)

    first_name = request.params.get('firstname', 'No first name')
    last_name = request.params.get('lastname', 'No last name')

    
    body = '<h1>Welcome %s %s </h1>' % (first_name, last_name)

    return Response(
        content_type="text/html",
        body=body
    )

@view_config(route_name='welcome')
def welcome_view(request):
    body = '<h1>Hello %(first)s %(last)s!</h1>' % request.matchdict
    return Response(
        content_type="text/html",
        body=body
    )

