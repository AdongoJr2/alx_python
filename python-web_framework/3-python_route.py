"""My module"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def home():
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    return 'HBNB'


@app.route('/c/<text>')
def dynamic_text(text):
    response = 'C {}'.format(text.replace('_', ' '))
    return response


@app.route('/python', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def dynamic_pyhton_text(text):
    response = 'Python {}'.format(text.replace('_', ' '))
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
