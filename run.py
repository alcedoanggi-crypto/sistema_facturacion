# Importamos la función que crea la app y el objeto db
from app import create_app, db

# Creamos la instancia de la aplicación llamando a la función
app = create_app()

if __name__ == '__main__':
    # Creamos el contexto de la aplicación para interactuar con la base de datos
    with app.app_context():
        # Crea las tablas definidas en tus modelos
        db.create_all()
        print("Tablas creadas exitosamente.")

    # Ejecutamos el servidor de desarrollo
    app.run(debug=True)