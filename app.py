from flask import Flask
from werkzeug.urls import url_q
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world"

if __name__ == '__main__':
    app.run(debug=True)