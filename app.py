from flask import Flaskhttps://github.com/estelanim/flaskapp/tree/main
app = Flask(__name__)

 

@app.route('/')
def hello_world():
    return 'Hello, Flask'
