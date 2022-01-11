from bottle import route, run, template, request
from pybot import pybot


@route('/hello')
def hello():
    return template('pybot_template', input_text='', output_text='')


@route('/hello', method='POST')
def do_hello():
    input_text = request.forms['input_text']
    input_image = request.files.input_image
    output_text = pybot(input_text, input_image)
    return template('pybot_template', input_text=input_text, output_text=output_text)


run(host='localhost', port=8080, debug=True)
