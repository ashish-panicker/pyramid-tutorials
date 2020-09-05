from pyramid.compat import escape
from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.view import view_config


@view_config(route_name='hello', renderer='hello.jinja2')
def hello_world(request):
    return dict(name=request.matchdict['name'])

@view_config(route_name='hello_json', renderer='json')
def hello_json(request):
    return {"name":"ashish", "email":"ashish.s.@easyskillup.com"}
