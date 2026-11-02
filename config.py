import os
from dotenv import load_dotenv

# Carga las variables del archivo .env
load_dotenv()

class Config:
    # Necesaria para sesiones y formularios; definir SECRET_KEY en el .env en producción
    SECRET_KEY = os.getenv('SECRET_KEY', 'cambiar-esta-clave-en-produccion')

    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_HOST = os.getenv('DB_HOST')
    DB_PORT = os.getenv('DB_PORT')
    DB_NAME = os.getenv('DB_NAME')

    # Ejemplo de cómo armar la cadena de conexión para SQLAlchemy o Psycopg2
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    # Tamaño máximo de archivos subidos (fotos de productos, Excel): 5 MB
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024