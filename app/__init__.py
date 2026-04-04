from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    # Redirigir al login si el usuario no está autenticado
    login_manager.login_view = 'main.login'
    login_manager.login_message = "Por favor inicia sesión para acceder."

    # Registro del Blueprint
    from app.routes import main
    app.register_blueprint(main)

    return app


@login_manager.user_loader
def load_user(user_id):
    from app.models.user import User
    return User.query.get(int(user_id))