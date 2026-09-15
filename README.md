# 📑 Sistema de Facturación Pro 🚀
> **Solución integral desarrollada en Python & PostgreSQL**

Este proyecto nace de la necesidad de centralizar y automatizar los procesos de facturación, permitiendo un control preciso sobre las ventas y clientes bajo una arquitectura robusta y escalable.

---

## 🖼️ Vista Previa del Sistema

<p align="center">
  <img src="docs/img/02-dashboard.png" alt="Panel de control del sistema" width="850">
</p>

<p align="center">
  <img src="docs/img/01-login.png" alt="Pantalla de inicio de sesión" width="270">
  <img src="docs/img/03-invoices.png" alt="Gestión de facturas" width="270">
  <img src="docs/img/04-customers.png" alt="Gestión de clientes" width="270">
</p>

<details>
<summary><strong>Ver más capturas</strong> (inventario, reportes y ticket de factura)</summary>
<br>

**Inventario de productos**
<img src="docs/img/05-products.png" alt="Inventario de productos">

**Reportes en PDF**
<img src="docs/img/07-reports.png" alt="Módulo de reportes">

**Ticket de factura impreso**
<img src="docs/img/06-invoice-ticket.png" alt="Ticket de factura" width="350">

</details>

---

## 💎 Características Estrella
*   **Gestión 360 de Clientes:** Registro detallado de la facturación.
*   **Arquitectura MVC:** Separación clara entre la lógica de negocio, datos y visualización para facilitar el mantenimiento.
*   **Persistencia Robusta:** Integración nativa con **PostgreSQL** para manejar grandes volúmenes de datos con integridad referencial.
*   **Interfaz Dinámica:** Renderizado de vistas fluidas utilizando el motor de plantillas Jinja2.

---

## ⚙️ Instalación y Puesta en Marcha

```bash
# 1. Clona el repositorio
git clone https://github.com/alcedoanggi-crypto/sistema_facturacion.git
cd sistema_facturacion

# 2. Crea y activa un entorno virtual
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Linux / macOS

# 3. Instala las dependencias
pip install -r requirements.txt
```

### 🗄️ Base de Datos

El proyecto incluye el archivo [`biling_db.sql`](biling_db.sql) con el esquema completo. Crea la base en PostgreSQL y ejecútalo:

```bash
psql -U tu_usuario -d nombre_db -f biling_db.sql
```

### 🔐 Variables de Entorno

Configura la conexión mediante variables de entorno (no uses credenciales en el código):

```bash
set SECRET_KEY=tu_clave_secreta          # Windows
set DATABASE_URL=postgresql://usuario:password@localhost:5432/billing_db
```

### ▶️ Ejecutar la Aplicación

```bash
python run.py
```

La aplicación quedará disponible en `http://127.0.0.1:5000`.

---
## 🛠️ Stack Tecnológico
| Tecnología | Función |
| :--- | :--- |
| **Python 3.x** | Motor de lógica principal |
| **PostgreSQL** | Almacenamiento y gestión de datos relacionales |
| **MVC** | Patrón de diseño de software |
| **Git/GitHub** | Control de versiones y despliegue |

---

## 🏗️ Estructura del Ecosistema
El sistema está organizado de forma modular para que cualquier desarrollador pueda entenderlo en segundos:

```text
sistema_facturacion/
├── app/
│   ├── models/       # 🗄️ El corazón de los datos (PostgreSQL)
│   ├── static/       # 🎨 Estilos y recursos visuales
│   ├── templates/    # 🖼️ Vistas HTML dinámicas
│   └── routes.py     # 🚦 El tráfico: Conecta usuario y datos
├── config.py         # 🔐 Seguridad y conexión a BD
├── main.py           # ⚡ Punto de ignición del sistema
└── run.py            # 🚀 Script de lanzamiento rápido
```

---

## 📄 Licencia

Este proyecto se distribuye bajo la licencia MIT. Eres libre de usarlo, modificarlo y distribuirlo.

## 👤 Autor

Desarrollado por **Anggie** — [GitHub](https://github.com/alcedoanggi-crypto)
