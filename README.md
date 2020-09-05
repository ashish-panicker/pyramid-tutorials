# Getting started with web development in python using pyramid

Pyramid is web development framwork in python that helps us to create a scalable web application.

Setting up pyramid in linux
```sh
# set an environment variable to where you want your virtual␣ environment
export VENV=~/pyramid/env

# create the virtual environment
$ python3 -m venv $VENV

# install pyramid
$ $VENV/bin/pip install pyramid

# exceute the application
$VENV/bin/python <path-to-app.py>
```
## Sample hello world application using pyramid

```sh
# Create the hello_world work directory
mkdir hello_world

# Create the app.py python file
touch hello_world/app.py
```

```python
'''
This is a simple hello world application.
'''
from waitress import serve
from pyramid.config import Configurator
from pyramid.response import Response

def  hello_world(request):
	print('URL: ' + request.url)
	name = request.params.get('name', 'No Name Provided')
	url = request.url
	body = '<h1>URL %s with name: %s</h1>' % (url, name)
	return Response(
		content_type="text/html",
		body=body
	)

if __name__ == '__main__': 
'''
Python’s way of saying ”Start here when running from the command line”.
'''
	with Configurator() as config:
		config.add_route('hello', '/')
		config.add_view(hello_world, route_name='hello')
		app = config.make_wsgi_app()
	serve(app, host='0.0.0.0', port=6543)
```
Run the helloworld application
```sh
# exceute the application
$VENV/bin/python ./hello_world/app.py
```
Browse to **http://localhost:6543/** to view the application.

##  Reading http request

Every request made by the client is sent an http request.

```python

'''
hello_world/app.py
The hello_world function is a ”view”. In Pyramid views are the primary way
to accept web requests and return responses.
'''
def hello_world(request):
	url = request.url
	'''
	 A single a request paramter
	 http://localhost:6543/?name=Shraddha
	
     A multi request paramter
	 http://localhost:6543/?name=Shraddha&location=USA
	'''
	name = request.params.get('name', 'No Name Provided')
	location= request.params.get('location', 'No Location Provided')
	body = 'URL %s with name: %s and location: %s' % (url, name, location)
	
	return Response(
		content_type="text/plain",
		body=body
	)
```
## Creating a multi views multi url demo
```python
'''
Create a folder called multi_view
Create the following files inside that folder app.py, views.py

add the following code in views.py
'''
from pyramid.compat import escape
from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.view import view_config

@view_config(route_name='home')
def  home_view(request):
	return Response('<p>Say <a href="/howdy?name=Ashish">Hello</a></p>') 
  
@view_config(route_name='hello')
def  hello_view(request):
	name = request.params.get('name', 'No Name')
	body = '<p>Hi %s, this <a href="/goto">redirects</a></p>'
	return Response(body % escape(name))

@view_config(route_name='redirect')
def  redirect_view(request):
	return HTTPFound(location="/problem")
	
@view_config(route_name = 'exception')
def  exception_view(request):
	raise  Exception()
```

```python
'''
add the following code in app.py
'''

from waitress import serve
from pyramid.config import Configurator
from pyramid.response import Response

if __name__ == '__main__':
	with Configurator() as config:
		config.add_route('home', '/')
		config.add_route('hello', '/howdy')
		config.add_route('redirect', '/goto')
		config.add_route('exception', '/problem')	
		config.scan('views')
		app = config.make_wsgi_app()
	serve(app, host='0.0.0.0', port=6543)
```
Exceute the applciation

```sh
# exceute the application
$VENV/bin/python ./multi_views/app.py
```

**@view_config** is used in declarative configuration where are **add_view()** is and example declarative configurarion

## More URL

Instead of using a query string parameters like http://localhost:6543/welcome?first=Ashish&last=Panicker what if wanted to use path values like http://localhost:6543/welcome/Ashish/Panicker


```python
'''
add the following code in the multi_views/views.py
'''

@view_config(route_name = 'welcome')
def welcome_view(request):
    body = '<h1>Hello %(first)s %(last)s!</h1>' % request.matchdict
    '''
    request.matchdict contains values from the URL that match the ”replacement patterns” (the curly braces) in the route declaration
    '''
    return Response(body)
```

```python
'''
add the following code in multi_views/app.py
'''

from waitress import serve
from pyramid.config import Configurator
from pyramid.response import Response

if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('home', '/')
        config.add_route('hello', '/howdy')
        config.add_route('redirect', '/goto')
        config.add_route('exception', '/problem')
        '''updated code'''
        config.add_route('welcome', '/welcome/{first}/{last}')
        config.scan('views')
        app = config.make_wsgi_app()
    serve(app, host='0.0.0.0', port=6543)

```

```sh
# Run the application as 
$VENV/bin/python ./multi_views/app.py
```

Browse to http://192.168.24.133:6543/welcome/ashish/s to see the output

## Templating

Insted of rendering raw html we can use a templating engine like jinja in pyramid.

```sh
# Install jinja2
$VENV/bin/pip install pyramid_jinja2

# Create a work directory
mkdir templated_views

# Create the python files
touch templated_views/app.py
touch templated_views/views.py

# Create jinja file
touch touch templated_views/hello.jinja2

```

```python
'''app.py'''
from waitress import serve
from pyramid.config import Configurator
from pyramid.response import Response

if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('hello', '/hello/{name}')
		'''include jinja2'''
        config.include('pyramid_jinja2')
        config.scan('views')
        app = config.make_wsgi_app()
    serve(app, host='0.0.0.0', port=6543)
```
```python
'''views.py'''
from pyramid.compat import escape
from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.view import view_config


@view_config(route_name='hello', renderer='hello.jinja2')
def hello_world(request):
    return dict(name=request.matchdict['name'])
```
```html
<!-- hello.jinja2 -->
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Hello World</title>
    </head>
    <body>
        <h1>Hello {{ name }}!</h1>
    </body>
</html>
```
```sh
# Execute the application and verify the output
$VENV/bin/python  ./templated_views/app.py 
```

## Adding static resources

Resources like css files, images are called static resources.
To accomplish this we use the **config.add_static_view(name='', path='')**

```sh
# Create a folder named static to host all the static resources
mkdir -p templated_views/static

# Add a css file into the templated_views project
touch templated_views/static/site.css
```

Add the following code into the static/site.css file

```css
/* Setting the default font and margin of the page. */
body {
    margin: 2em;
    font-family: sans-serif;
}

/* Aligning the h1 text to center. */
h1 {
    text-align: center;
}
```

Add the following line inside the head element of hello.jinja2
```html
<link rel="stylesheet" href="/static/site.css"/>
```

Update the app.py file
```python
from waitress import serve
from pyramid.config import Configurator
from pyramid.response import Response

if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('hello', '/hello/{name}')
		'''modified line'''
        config.add_static_view(name='static', path='static')
        config.include('pyramid_jinja2')
        config.scan('views')
        app = config.make_wsgi_app()
    serve(app, host='0.0.0.0', port=6543)
```
## JSON responses

Web applications can send more than HTML as its response, modern web applciations can send data in JSON format, especially useful when creating REST api's

Add the following route in the **views.py** file
```python

'''views.py'''
@view_config(route_name='hello_json', renderer='json')
def hello_json(request):
    return [1, 2, 3]
```
Add the following route in the **app.py** file

```python
config.add_route('hello_json', '/hello.json')
```

Run the application
```sh
# Execute the application and verify the output
$VENV/bin/python  ./templated_views/app.py 
```

## References

[Configurator docs](https://docs.pylonsproject.org/projects/pyramid/en/latest/api/config.html)
[add_route()](https://docs.pylonsproject.org/projects/pyramid/en/latest/api/config.html#pyramid.config.Configurator.add_route)
[request_object](https://docs.pylonsproject.org/projects/pyramid/en/latest/narr/webob.html?highlight=request#request)
[@view_config](https://docs.pylonsproject.org/projects/pyramid/en/latest/api/view.html#pyramid.view.view_config)