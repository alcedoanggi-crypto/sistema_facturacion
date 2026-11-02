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

## 🎬 Video del Sistema

<p align="center">
  <img src="docs/video/recorrido-sistema.gif" alt="Recorrido por el sistema" width="800">
</p>

<p align="center">
  <a href="docs/video/recorrido-sistema.mp4"><strong>▶ Ver el video completo en MP4</strong></a>
</p>

## 📸 Vista Previa

<p align="center">
  <img src="docs/screenshots/dashboard.png" alt="Panel de control" width="850">
</p>

<p align="center">
  <img src="docs/screenshots/login.png" alt="Inicio de sesión" width="270">
  <img src="docs/screenshots/facturas.png" alt="Listado de facturas" width="270">
  <img src="docs/screenshots/clientes.png" alt="Gestión de clientes" width="270">
</p>

**Inventario de productos con fotos**
<img src="docs/screenshots/productos.png" alt="Inventario de productos">

<details>
<summary><strong>Ver más capturas</strong> (formularios, detalle de factura, reportes, ticket y usuarios)</summary>
<br>

**Nuevo producto con foto y vista previa**
<img src="docs/screenshots/producto-nuevo.png" alt="Formulario de nuevo producto">

**Crear factura**
<img src="docs/screenshots/factura-nueva.png" alt="Formulario de nueva factura">

**Detalle de factura**
<img src="docs/screenshots/factura-detalle.png" alt="Detalle de factura">

**Reportes en PDF**
<img src="docs/screenshots/reportes.png" alt="Módulo de reportes">

**Ticket de factura impreso**
<img src="docs/screenshots/ticket-factura.png" alt="Ticket de factura">

**Usuarios y roles**
<img src="docs/screenshots/configuracion.png" alt="Configuración de usuarios">

</details>

---

## 🚀 Características Principales

- **Gestión de clientes:** registro y control de datos fiscales/contacto.
- **Catálogo de productos/servicios:** con precio, código de barras, foto
  del producto e importación masiva desde Excel.
- **Control de inventario:** cada factura descuenta el stock, no permite
  vender más de lo disponible y lo devuelve al editar o anular la factura.
- **Generación de facturas:** cálculo automático de subtotal, impuestos y
  total; numeración correlativa de comprobantes.
- **Exportación a PDF:** generación de la factura lista para enviar al
  cliente.
- **Historial de ventas:** consulta de facturas emitidas por fecha o cliente.
- **Autenticación de usuarios:** control de acceso, alta de usuarios con rol (Administrador / Vendedor)
  y contraseñas encriptadas para los usuarios nuevos.

## 🛠️ Tecnologías Utilizadas

| Categoría        | Tecnología                                   |
|-------------------|-----------------------------------------------|
| Backend           | Python 3.11 + Flask                           |
| Base de datos     | PostgreSQL (gestionada con Flask-SQLAlchemy)  |
| Frontend          | HTML5 (Jinja2), CSS3, JavaScript              |
| Generación de PDF | FPDF2                                         |
| Seguridad         | Variables de entorno (python-dotenv)          |

## 📁 Estructura del Proyecto

```
sistema_facturacion/
├── app/
│   ├── models/          # Cliente, Producto, Factura, Usuario
│   ├── static/          # CSS, JS y recursos estáticos
│   ├── templates/       # Vistas Jinja2 (facturas, clientes, productos)
│   └── routes.py        # Lógica de navegación y generación de comprobantes
├── docs/screenshots/    # Capturas usadas en este README
├── biling_db.sql        # Esquema de la base de datos PostgreSQL
├── config.py            # Configuración segura del servidor
├── requirements.txt     # Dependencias del proyecto
└── run.py               # Punto de entrada de la aplicación
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

Define las siguientes variables (por ejemplo en un archivo `.env` cargado con
`python-dotenv`, o directamente en tu shell):

```env
SECRET_KEY=tu_clave_secreta_aqui
DATABASE_URL=postgresql://usuario:password@localhost:5432/billing_db
```

### 5. Crear la base de datos

Crea la base en PostgreSQL y aplica el esquema incluido:

```bash
psql -U tu_usuario -d billing_db -f biling_db.sql
```

### 6. Ejecutar la aplicación

```bash
python run.py
```

Al iniciar, `run.py` crea automáticamente las tablas que falten y levanta el
servidor en `http://127.0.0.1:5000`.

> Para tener acceso, crea un usuario directamente en la tabla `user` (o desde
> el módulo **Configuración** una vez dentro del sistema con un usuario
> existente).

> **Actualización desde una versión anterior:** si tu base ya existía, agrega
> la columna de fotos de productos:
>
> ```sql
> ALTER TABLE products ADD COLUMN image VARCHAR(255);
> ```

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
