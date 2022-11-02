from flask import Flask, g
from flask_cors import CORS

# Database
import models

# models
from resources.users import user

# login manager
from flask_login import LoginManager


DEBUG = True
PORT = 8000

app = Flask(__name__)

app.secret_key = "aajn23-/fu919"
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

CORS(user, origins=['https://localhost:3000'], supports_credentials=True)
app.register_blueprint(user, url_prefix="/api/v1/auctions/users")

#default route
@app.route('/api/v1/auctions')
def index():
    """Home Route"""
    return "hello world"

if __name__ == "__main__":
    models.initialize()
    app.run(debug=DEBUG, port=PORT)