# app/models/user.py
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin, db.Model):
    __tablename__ = 'user'  # Buena práctica definirlo siempre
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    role = db.Column(db.String(50), nullable=False, default='consulta')

    def check_password(self, password_ingresada):
        # Comparación directa de texto plano como tienes en tu BD
        return self.password == password_ingresada