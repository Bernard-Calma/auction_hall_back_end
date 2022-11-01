from flask import Flask

DEBUG = True
PORT = 8000

app = Flask(__name__)

#default route
@app.route('/api/v1/auctions')
def index():
    return "hello world"

if __name__ == "__main__":
    app.run(debug=DEBUG, port=PORT)