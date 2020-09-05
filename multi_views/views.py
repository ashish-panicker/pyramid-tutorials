from pyramid.compat import escape
from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.view import view_config


@view_config(route_name='home')
def home_view(request):
    return Response('<p>Say <a href="/howdy?name=Ashish">Hello</a></p>')


@view_config(route_name='hello')
def hello_view(request):
    name = request.params.get('name', 'No Name')
    body = '<p>Hi %s, this <a href="/goto">redirects</a></p>'
    return Response(body % escape(name))

@view_config(route_name='redirect')
def redirect_view(request):
    return HTTPFound(location="/problem")

@view_config(route_name = 'exception')
def exception_view(request):
    raise Exception()

@view_config(route_name = 'welcome')
def welcome_view(request):
    body = '<h1>Hello %(first)s %(last)s!</h1>' % request.matchdict
    return Response(body)
