from flask import Flask
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "Hello Rhez zellyace25 password: ..."

if __name__ == '__main__':
    app.run()