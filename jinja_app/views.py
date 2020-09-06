from pyramid.compat import escape
from pyramid.response import Response
from pyramid.view import view_config

@view_config(route_name='index', renderer='index.jinja2')
def index_view(request):
    return dict()
