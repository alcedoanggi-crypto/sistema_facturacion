# app/models/product.py
from app import db


# Busca la clase Product y añade esta línea:
class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)

    # AÑADE ESTA LÍNEA AQUÍ:
    barcode = db.Column(db.String(50), unique=True, nullable=True)

    # Ruta relativa a /static de la foto del producto (ej: uploads/products/abc.jpg)
    image = db.Column(db.String(255), nullable=True)