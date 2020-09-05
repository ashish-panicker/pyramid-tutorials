from waitress import serve
from pyramid.config import Configurator
from pyramid.response import Response


def operate(request):
    print('URL: ' + request.url)

    num1 = request.params.get('num1', '0')
    num2 = request.params.get('num2', '0')
    oper = request.params.get('oper', 'none')

    if oper == 'add':
        body = '<h1> %d +  %d = %d</h1>' % (int(num1), int(num2), (int(num1) + int(num2)))
        return Response(
            content_type="text/html",
            body=body
        )


if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('operate', '/')
        config.add_view(operate, route_name='operate')
        app = config.make_wsgi_app()
    serve(app, host='0.0.0.0', port=6543)
