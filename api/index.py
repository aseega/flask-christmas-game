from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    x = 1
    y = 2
    if x = y:
        return 'Hello, World!'
    else:
        return x

@app.route('/about')
def about():
    return 'About'
10