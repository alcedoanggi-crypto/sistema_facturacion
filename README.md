# 🧾 Sistema de Facturación Electrónica

Aplicación web para la gestión de facturación de un negocio: clientes,
productos, generación de comprobantes y control de ventas.

Este proyecto demuestra desarrollo backend con **Python y Flask**,
arquitectura **MVC**, y persistencia de datos con **PostgreSQL**.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Flask](https://img.shields.io/badge/Flask-2.x-black)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue)
![License](https://img.shields.io/badge/license-MIT-green)

---

## 📸 Vista Previa

> Agrega aquí 2-3 capturas de pantalla (listado de facturas, formulario de
> nueva factura, vista de factura generada en PDF).
>
> ```markdown
> ![Listado de facturas](docs/screenshots/facturas.png)
> ![Nueva factura](docs/screenshots/nueva-factura.png)
> ```

**Demo en vivo:** _(agrega aquí el link si despliegas en Render/Railway)_

---

## 🚀 Características Principales

- **Gestión de clientes:** registro y control de datos fiscales/contacto.
- **Catálogo de productos/servicios:** con precio unitario e impuestos.
- **Generación de facturas:** cálculo automático de subtotal, impuestos y
  total; numeración correlativa de comprobantes.
- **Exportación a PDF:** generación de la factura lista para enviar al
  cliente.
- **Historial de ventas:** consulta de facturas emitidas por fecha o cliente.
- **Autenticación de usuarios:** control de acceso al sistema.

## 🛠️ Tecnologías Utilizadas

| Categoría        | Tecnología                                   |
|-------------------|-----------------------------------------------|
| Backend           | Python 3.11 + Flask                           |
| Base de datos     | PostgreSQL (gestionada con Flask-SQLAlchemy)  |
| Frontend          | HTML5 (Jinja2), CSS3, JavaScript              |
| Generación de PDF | ReportLab / WeasyPrint (según implementación) |
| Seguridad         | Variables de entorno (python-dotenv)          |

## 📁 Estructura del Proyecto

```
sistema_facturacion/
├── app/
│   ├── static/        # CSS, JS y recursos estáticos
│   ├── templates/      # Vistas Jinja2 (facturas, clientes, productos)
│   ├── models.py       # Estructura de la base de datos (Cliente, Producto, Factura)
│   └── routes.py       # Lógica de navegación y generación de comprobantes
├── config.py            # Configuración segura del servidor
├── requirements.txt      # Dependencias del proyecto
├── run.py                # Punto de entrada de la aplicación
└── .env.example           # Ejemplo de variables de entorno requeridas
```

---

## 🔧 Instalación y Uso Local

### 1. Clonar el repositorio

```bash
git clone https://github.com/alcedoanggi-crypto/sistema_facturacion.git
cd sistema_facturacion
```

### 2. Crear y activar entorno virtual

```bash
python -m venv venv

# En Linux/Mac
source venv/bin/activate

# En Windows
venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno

Crea un archivo `.env` en la raíz del proyecto basado en `.env.example`:

```env
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=tu_clave_secreta_aqui
DATABASE_URL=postgresql://usuario:password@localhost:5432/facturacion_db
```

### 5. Crear la base de datos y aplicar migraciones

```bash
flask db upgrade
```

> Si el proyecto no usa Flask-Migrate todavía, inicializa las tablas con:
> `python -c "from app import db; db.create_all()"`

### 6. (Opcional) Cargar datos de prueba

```bash
python seed.py
```

### 7. Ejecutar la aplicación

```bash
flask run
```

La aplicación estará disponible en `http://127.0.0.1:5000`

**Credenciales de prueba** _(si aplica)_:
- Usuario: `admin@demo.com`
- Contraseña: `demo1234`

---

## 🧪 Próximas Mejoras

- [ ] Envío automático de factura por correo al cliente
- [ ] Integración con pasarela de pago
- [ ] Tests automatizados con Pytest
- [ ] Despliegue con Docker

## 👩‍💻 Autora

**Anggie Alcedo** — Ingeniera de Sistemas | Full Stack Developer & QA
Automation
[GitHub](https://github.com/alcedoanggi-crypto) ·
[LinkedIn](#) · alcedoanggi@gmail.com

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Ver el archivo `LICENSE` para más
detalles.
