from flask import Flask
from flask import escape, url_for

app = Flask(__name__)

@app.route('/index')
@app.route('/home')
@app.route('/')
def hello():
    return "<h1>Hello Totoro!</h1><img src='http://helloflask.com/totoro.gif'>"

@app.route('/user/<name>')
def user_page(name):
    return 'hello, {}'.format(escape(name))

@app.route('/test')
def test_url_for():
    print(url_for('hello'))
    print(url_for('user_page', name='huanghao'))
    print(url_for('test_url_for', num=2))
    return 'test page.'