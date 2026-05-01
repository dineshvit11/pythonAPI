from flask import Flask
from flask_cors import CORS
from flask_bcrypt import Bcrypt

from config import Config
from db import mysql

from routes.auth_routes import auth_bp
from routes.user_routes import user_bp
from routes.product_routes import product_bp
from routes.cart_routes import cart_bp

app = Flask(__name__)

app.config.from_object(Config)

mysql.init_app(app)

bcrypt = Bcrypt(app)

CORS(app, resources={
    r"/api/*": {
        "origins": "http://localhost:3000"
    }
})

app.register_blueprint(auth_bp)
app.register_blueprint(user_bp)
app.register_blueprint(product_bp)
app.register_blueprint(cart_bp)


@app.route('/')
def home():
    return {
        "message": "Secure Flask API Running"
    }


if __name__ == '__main__':
    app.run(debug=True, port=8000)
