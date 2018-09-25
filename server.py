from japronto import Application
import jinja2
import japronto_jinja2
import controllers
import os

"""
import os
import jinja2
import japronto_jinja2
from japronto import Application


CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))


def hello(request):
    return request.Response(text='Hello world!')


@japronto_jinja2.template('index.html')
def index(request):
    context = {'first_name': 'Ja', 'second_name': 'Pronto'}
    return context


def index_manual_response(request):
    context = {'first_name': 'Obi', 'second_name': 'Wan'}
    response = japronto_jinja2.render_template('index.html', request, context)
    return response


app = Application()
templates_dir = os.path.join(CURRENT_DIR, 'templates')
japronto_jinja2.setup(app, loader=jinja2.FileSystemLoader(templates_dir))
app.router.add_route('/', hello)
app.router.add_route('/index', index)
app.router.add_route('/one', index_manual_response)
app.run(debug=True)


"""

CUR_DIR = os.path.dirname(os.path.realpath(__file__))

@japronto_jinja2.template('index.html')
def hello(request):
    return {'blah':'blah'}

templates = os.path.join(CUR_DIR,"templates")

app = Application()
japronto_jinja2.setup(app,loader=jinja2.FileSystemLoader(templates))
app.router.add_route('/', hello,methods=["GET"])

app.run(port=8888,debug=True)