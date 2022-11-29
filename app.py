from flask import Flask, g, jsonify
from flask_cors import CORS


import os
from dotenv import load_dotenv

# Database
import models

# models
from resources.users import user
from resources.auctions import auctions

# login manager
from flask_login import LoginManager


DEBUG = True
PORT = 8000

app = Flask(__name__)

# Error Handler
@app.errorhandler(Exception)
def server_error(err):
    """This function to display errors on routes"""
    ## This logs error uncomment to enable
    # app.logger.exception(err) 
    return jsonify(
        data = {},
        status = {
            "code": 400,
            "message": f"Error: {err}"
        }
    ), 400

app.secret_key = os.environ.get("SECRET_KEY")
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    """set up user object"""
    try:
        return models.User.get(models.User.id == user_id)
    except:
        return None

@app.before_request
def before_request():
    """Connect to the database before each request."""
    g.db = models.DATABASE
    g.db.connect()

@app.after_request
def after_request(response):
    """Close the database connection after each request"""
    g.db.close()
    return response

CORS(user, origins=['https://localhost:8081'], supports_credentials=True)
app.register_blueprint(user, url_prefix="/api/v1/auctions/users")
app.register_blueprint(auctions, url_prefix = "/api/v1/auctions")

#default route
@app.route('/api/v1/auctions')
def index():
    """Home Route"""
    return "hello world"

if os.environ.get('FLASK_ENV') != 'development':
  print('\non heroku!')
  models.initialize()

if __name__ == "__main__":
    models.initialize()
    print(f"Server is up and running at PORT: {PORT}")
    # print("Debug", DEBUG)
    app.run(debug=DEBUG, port=PORT)
    


