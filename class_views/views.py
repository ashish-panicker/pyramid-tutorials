from pyramid.compat import escape
from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.view import view_config, view_defaults

@view_defaults(route_name='hello')
class HelloViews:
    def __init__(self, request):
        self.name = request.matchdict['name']

    @view_config(renderer='hello.jinja2')
    def hello_view(self, request):
        return dict()

    @view_config(request_param='form.edit', renderer='edit.jinja2')
    def edit_view(self):
        print('edit view')
        return dict()

    @view_config(request_param='form.delete', renderer='delete.jinja2')
    def delete_view(self):
        print('delete')
        return dict()
