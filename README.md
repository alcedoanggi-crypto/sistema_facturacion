# 📑 Sistema de Facturación Pro 🚀
> **Solución integral desarrollada en Python & PostgreSQL**

Este proyecto nace de la necesidad de centralizar y automatizar los procesos de facturación, permitiendo un control preciso sobre las ventas y clientes bajo una arquitectura robusta y escalable.

---

## 💎 Características Estrella
*   **Gestión 360 de Clientes:** Registro detallado de la facturación.
*   **Arquitectura MVC:** Separación clara entre la lógica de negocio, datos y visualización para facilitar el mantenimiento.
*   **Persistencia Robusta:** Integración nativa con **PostgreSQL** para manejar grandes volúmenes de datos con integridad referencial.
*   **Interfaz Dinámica:** Renderizado de vistas fluidas utilizando el motor de plantillas Jinja2.

---
## 🔒 Seguridad y Buenas Prácticas
Este proyecto implementa estándares de seguridad para el manejo de credenciales:
*   **Variables de Entorno:** Uso de `python-dotenv` para evitar el "hardcoding" de credenciales en el código fuente.
*   **GitIgnore:** El archivo `.env` está excluido del control de versiones para proteger los accesos a la base de datos PostgreSQL.
*   **Configuración Segura:** Se incluye un archivo `.env.example` como plantilla para despliegues locales sin comprometer la seguridad.
---
🗄️ Base de Datos
El proyecto incluye un archivo database_schema.sql. Para replicar la base de datos, crea una base en PostgreSQL y ejecuta:
psql -U tu_usuario -d nombre_db -f database_schema.sql

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
