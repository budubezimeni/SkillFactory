from flask import Flask, request
import datetime
app = Flask(__name__)


@app.route('/hello')
def hello_func():
    name = request.args.get('name')
    return f'hello {name}!'

@app.route('/time')
def current_time():
    return {'time': datetime.datetime.now()}

if __name__ == '__main__':
    app.run('localhost', 5000)
