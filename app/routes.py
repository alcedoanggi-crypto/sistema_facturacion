from flask import Blueprint, render_template, redirect, url_for, flash, request, make_response
from flask_login import login_user, logout_user, login_required, current_user
from app import db
from app.models.user import User
from app.models import Invoice, Customer, Product, InvoiceItem
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DecimalField, IntegerField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email
from datetime import datetime
import pandas as pd
from flask import Response
import io
from fpdf import FPDF
from sqlalchemy import func
from datetime import datetime, timedelta
from collections import OrderedDict

main = Blueprint('main', __name__)


# --- FORMULARIOS ---

class LoginForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Ingresar')


# --- RUTAS DE ACCESO ---

@main.route('/')
def index():
    return redirect(url_for('main.dashboard'))


@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form.get('username')).first()
        if user and user.check_password(request.form.get('password')):
            login_user(user)
            return redirect(url_for('main.dashboard'))
        flash('Credenciales inválidas', 'danger')
    return render_template('login.html')


@main.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.login'))


@main.route('/dashboard')
@login_required
def dashboard():
    todas_facturas = Invoice.query.all()
    count_clientes = Customer.query.count()
    count_productos = Product.query.count()
    total_ventas = sum(i.total for i in todas_facturas) if todas_facturas else 0

    # Lógica de gráfica: Ventas por día
    ventas_diarias = db.session.query(
        db.func.date(Invoice.date_created).label('fecha'),
        db.func.sum(Invoice.total).label('total')
    ).group_by('fecha').order_by('fecha').limit(10).all()

    labels_ventas = [str(v.fecha) for v in ventas_diarias] if ventas_diarias else ["Sin datos"]
    data_ventas = [float(v.total) for v in ventas_diarias] if ventas_diarias else [0]

    return render_template('dashboard.html',
                           total_ventas=total_ventas,
                           count_clientes=count_clientes,
                           count_productos=count_productos,
                           ultimas_facturas=Invoice.query.join(Customer).order_by(Customer.name.asc()).limit(5).all(),
                           labels_ventas=labels_ventas,
                           data_ventas=data_ventas)


# Simulamos la obtención de datos para el dashboard
def get_dashboard_stats():
    # 1. Crear el rango de los últimos 7 días
    hoy = datetime.now()
    labels_ventas = []
    data_ventas = []

    # Supongamos que estas son tus ventas reales de la DB
    # formato: {'2026-04-03': 4081.0, '2026-04-01': 500.0}
    ventas_reales = {venta.fecha.strftime('%Y-%m-%d'): venta.total for venta in facturas_db}

    for i in range(6, -1, -1):
        dia = (hoy - timedelta(days=i)).strftime('%Y-%m-%d')
        labels_ventas.append(dia)
        # Si el día existe en la DB ponemos el total, si no, ponemos 0
        data_ventas.append(ventas_reales.get(dia, 0))

    return labels_ventas, data_ventas

# --- MÓDULO DE CLIENTES (MODALES) ---

@main.route('/customers')
@login_required
def customers():
    return render_template('customers.html', customers=Customer.query.all())


@main.route('/add_customer', methods=['POST'])
@login_required
def add_customer():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    address = request.form.get('address')

    if name and email:
        new_c = Customer(name=name, email=email, phone=phone, address=address)
        db.session.add(new_c)
        db.session.commit()
        flash('Cliente agregado con éxito', 'success')
    return redirect(url_for('main.customers'))


@main.route('/customers/edit/<int:id>', methods=['POST'])
@login_required
def edit_customer(id):
    customer = Customer.query.get_or_404(id)
    customer.name = request.form.get('name')
    customer.email = request.form.get('email')
    customer.phone = request.form.get('phone')
    customer.address = request.form.get('address')
    db.session.commit()
    flash('Cliente actualizado', 'success')
    return redirect(url_for('main.customers'))


@main.route('/customers/delete/<int:id>', methods=['POST'])
@login_required
def delete_customer(id):
    customer = Customer.query.get_or_404(id)
    db.session.delete(customer)
    db.session.commit()
    flash('Cliente eliminado', 'warning')
    return redirect(url_for('main.customers'))


# --- MÓDULO DE PRODUCTOS ---

@main.route('/products')
@login_required
def products():
    return render_template('products.html', products=Product.query.all())


@main.route('/products/add', methods=['POST'])
@login_required
def add_product():
    # Capturamos el nuevo campo 'barcode' del formulario
    barcode_val = request.form.get('barcode')

    new_p = Product(
        name=request.form.get('name'),
        barcode=barcode_val,  # <-- Agregado
        description=request.form.get('description'),
        price=float(request.form.get('price') or 0),
        stock=int(request.form.get('stock') or 0)
    )
    db.session.add(new_p)
    db.session.commit()
    flash('Producto guardado con éxito', 'success')
    return redirect(url_for('main.products'))


@main.route('/products/edit/<int:id>', methods=['POST'])
@login_required
def edit_product(id):
    product = Product.query.get_or_404(id)

    # Actualizamos los campos, incluyendo el código de barras
    product.name = request.form.get('name')
    product.barcode = request.form.get('barcode')  # <-- Agregado
    product.description = request.form.get('description')
    product.price = float(request.form.get('price') or 0)
    product.stock = int(request.form.get('stock') or 0)

    db.session.commit()
    flash('Producto actualizado correctamente', 'success')
    return redirect(url_for('main.products'))

@main.route('/products/delete/<int:id>', methods=['POST'])
@login_required
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    flash('Producto eliminado', 'warning')
    return redirect(url_for('main.products'))


@main.route('/products/import', methods=['POST'])
@login_required
def import_products():
    if 'file' not in request.files:
        flash('No se seleccionó ningún archivo', 'danger')
        return redirect(url_for('main.products'))

    file = request.files['file']

    if file.filename == '':
        flash('El nombre del archivo está vacío', 'danger')
        return redirect(url_for('main.products'))

    if file:
        try:
            # Leemos el Excel directamente a un DataFrame de Pandas
            df = pd.read_excel(file)

            # Validamos que las columnas necesarias existan (ajusta según tus nombres en el Excel)
            # El Excel debería tener columnas: barcode, name, description, price, stock
            for index, row in df.iterrows():
                new_p = Product(
                    barcode=str(row['barcode']) if 'barcode' in df.columns else None,
                    name=str(row['name']),
                    description=str(row['description']) if 'description' in df.columns else None,
                    price=float(row['price'] or 0),
                    stock=int(row['stock'] or 0)
                )
                db.session.add(new_p)

            db.session.commit()
            flash(f'¡Éxito! Se han importado {len(df)} productos.', 'success')

        except Exception as e:
            db.session.rollback()
            flash(f'Error al procesar el archivo: {str(e)}', 'danger')

    return redirect(url_for('main.products'))

# --- MÓDULO DE FACTURAS (CORREGIDO) ---

@main.route('/invoices')
@login_required
def invoices():  # Antes decía invoices_list
    return render_template('invoices.html',
                           invoices=Invoice.query.order_by(Invoice.date_created.desc()).all(),
                           customers=Customer.query.all(),
                           products=Product.query.all())


@main.route('/invoices/add', methods=['POST'])
@login_required
def add_invoice(): # <--- Antes decía add_invoice_post
    customer_id = request.form.get('customer_id')
    if not customer_id:
        flash('Error: Seleccione un cliente', 'danger')
        return redirect(url_for('main.invoices'))

    new_inv = Invoice(customer_id=customer_id, date_created=datetime.now(), total=0)


@main.route('/invoices/edit/<int:id>', methods=['POST'])
@login_required
def edit_invoice(id):  # Cambiamos el nombre aquí para que coincida con el HTML
    invoice = Invoice.query.get_or_404(id)

    # 1. Eliminamos los items anteriores para reemplazarlos por los nuevos
    InvoiceItem.query.filter_by(invoice_id=id).delete()

    # 2. Actualizamos el cliente
    invoice.customer_id = request.form.get('customer_id')

    total_acumulado = 0
    all_prods = Product.query.all()

    # 3. Procesamos los productos seleccionados en el modal de edición
    for p in all_prods:
        if request.form.get(f'product_{p.id}'):
            qty = int(request.form.get(f'quantity_{p.id}', 0))
            if qty > 0:
                item = InvoiceItem(
                    invoice_id=id,
                    product_id=p.id,
                    quantity=qty,
                    price=p.price
                )
                total_acumulado += (p.price * qty)
                db.session.add(item)

    # 4. Actualizamos el total de la factura
    invoice.total = total_acumulado
    db.session.commit()

    flash('Factura actualizada correctamente', 'success')
    return redirect(url_for('main.invoices'))


@main.route('/invoices/delete/<int:id>', methods=['POST'])
@login_required
def delete_invoice(id):
    invoice = Invoice.query.get_or_404(id)
    db.session.delete(invoice)
    db.session.commit()
    flash('Factura eliminada', 'warning')
    return redirect(url_for('main.invoices'))

@main.route('/invoices/print/<int:id>')
@login_required
def print_invoice(id):
    invoice = Invoice.query.get_or_404(id)
    # Calculamos el subtotal asumiendo que el total ya incluye IVA (ejemplo 16% o el que aplique)
    # Según tu imagen, el item dice "Exento", así que el subtotal es igual al total.
    return render_template('print_ticket.html', invoice=invoice)


# --- MÓDULO DE REPORTES ---

@main.route('/reports')
@login_required
def reports():
    total_clientes = Customer.query.count()
    total_productos = Product.query.count()
    total_facturas = Invoice.query.count()
    monto_total = db.session.query(db.func.sum(Invoice.total)).scalar() or 0
    return render_template('reports.html', total_clientes=total_clientes,
                           total_productos=total_productos, total_facturas=total_facturas,
                           monto_total=monto_total)


# --- FUNCIÓN AUXILIAR PARA GENERAR PDF ---

class PDF(FPDF):
    def header(self):
        # Banner azul superior
        self.set_fill_color(41, 128, 185)
        self.rect(0, 0, 210, 40, 'F')

        self.set_font('Arial', 'B', 20)
        self.set_text_color(255, 255, 255)
        self.set_y(10)
        self.cell(0, 15, 'SISTEMA DE GESTIÓN STOCKPRO', 0, 1, 'C')  # Centrado en el banner

        self.set_font('Arial', 'I', 10)
        self.cell(0, 5, 'Reporte Automatizado de Actividad', 0, 1, 'C')
        self.ln(20)

    def footer(self):
        # Pie de página con numeración
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f'Página {self.page_no()} / {{nb}}', 0, 0, 'C')
        # Fecha en el pie (opcional, ya la pondremos arriba)
        self.cell(0, 10, datetime.now().strftime("%d/%m/%Y"), 0, 0, 'R')


def generar_pdf_creativo(titulo, columnas, datos):
    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.add_page()

    # --- AJUSTE DE TÍTULO CENTRADO Y FECHA A LA DERECHA ---
    pdf.set_y(45)

    # 1. Título Centrado
    pdf.set_font('Arial', 'B', 16)
    pdf.set_text_color(44, 62, 80)
    pdf.cell(0, 10, titulo.upper(), 0, 1, 'C')

    # 2. Fecha alineada a la derecha
    pdf.set_font('Arial', '', 10)
    pdf.set_text_color(128, 128, 128)
    fecha_texto = f"Fecha de emisión: {datetime.now().strftime('%d/%m/%Y %H:%M')}"
    pdf.cell(0, 8, fecha_texto, 0, 1, 'R')  # 'R' para alinear a la derecha
    pdf.ln(5)

    # Configuración de Tabla
    ancho_total = 190
    ancho_col = ancho_total / len(columnas)

    # Encabezados de Tabla
    pdf.set_font('Arial', 'B', 11)
    pdf.set_fill_color(52, 73, 94)
    pdf.set_text_color(255, 255, 255)

    for col in columnas:
        col_clean = col.encode('latin-1', 'replace').decode('latin-1')
        pdf.cell(ancho_col, 10, col_clean, 1, 0, 'C', True)
    pdf.ln()

    # Cuerpo de la Tabla (Efecto Cebra)
    pdf.set_font('Arial', '', 10)
    pdf.set_text_color(0, 0, 0)

    for i, fila in enumerate(datos):
        fill = (i % 2 == 0)
        if fill: pdf.set_fill_color(245, 245, 245)

        for item in fila:
            texto = str(item).encode('latin-1', 'replace').decode('latin-1')
            pdf.cell(ancho_col, 8, texto, 1, 0, 'C', fill)
        pdf.ln()

    return pdf.output(dest='S')


# --- RUTAS DE EXPORTACIÓN CORREGIDAS ---

@main.route('/reports/export/customers')
@login_required
def export_customers_pdf():
    try:
        clientes = Customer.query.all()
        columnas = ["ID", "Nombre", "Email", "Telefono"]
        datos = [[str(c.id), c.name, c.email, c.phone or 'N/A'] for c in clientes]
        pdf_bytes = generar_pdf_creativo("Reporte de Clientes Registrados", columnas, datos)
        res = make_response(bytes(pdf_bytes))
        res.headers['Content-Type'] = 'application/pdf'
        return res
    except Exception as e:
        flash(f"Error: {str(e)}", "danger")
        return redirect(url_for('main.reports'))

@main.route('/reports/export/products')
@login_required
def export_products_pdf():
    try:
        prods = Product.query.all()
        columnas = ["Cod. Barras", "Nombre", "Precio", "Stock"]
        datos = [[p.barcode or 'N/A', p.name, f"$ {p.price:,.2f}", str(p.stock)] for p in prods]
        pdf_bytes = generar_pdf_creativo("Inventario de Productos en Existencia", columnas, datos)
        res = make_response(bytes(pdf_bytes))
        res.headers['Content-Type'] = 'application/pdf'
        return res
    except Exception as e:
        flash(f"Error: {str(e)}", "danger")
        return redirect(url_for('main.reports'))

@main.route('/reports/export/invoices')
@login_required
def export_invoices_pdf():
    try:
        facturas = Invoice.query.all()
        columnas = ["ID", "Fecha", "Cliente", "Total"]
        datos = [[str(i.id), i.date_created.strftime('%d/%m/%Y'), i.customer.name, f"$ {i.total:,.2f}"] for i in facturas]
        pdf_bytes = generar_pdf_creativo("Histórico de Ventas y Facturación", columnas, datos)
        res = make_response(bytes(pdf_bytes))
        res.headers['Content-Type'] = 'application/pdf'
        return res
    except Exception as e:
        flash(f"Error: {str(e)}", "danger")
        return redirect(url_for('main.reports'))

# --- MÓDULO DE CONFIGURACIÓN Y USUARIOS ---

@main.route('/settings')
@login_required
def settings():
    # Solo el administrador debería ver esto (puedes añadir lógica de roles luego)
    users = User.query.all()
    return render_template('settings.html', users=users)


@main.route('/settings/user/add', methods=['POST'])
@login_required
def add_user():
    username = request.form.get('username')
    password = request.form.get('password')
    role = request.form.get('role')  # Ejemplo: 'ADMIN' o 'VENDEDOR'

    if username and password:
        # Asumiendo que tu modelo User tiene un método para encriptar
        new_user = User(username=username, role=role)
        new_user.set_password(password)

        db.session.add(new_user)
        db.session.commit()
        flash(f'Usuario {username} creado con éxito', 'success')

    return redirect(url_for('main.settings'))


@main.route('/settings/user/delete/<int:id>', methods=['POST'])
@login_required
def delete_user(id):
    if current_user.id == id:
        flash('No puedes eliminarte a ti mismo', 'danger')
        return redirect(url_for('main.settings'))

    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    flash('Usuario eliminado', 'warning')
    return redirect(url_for('main.settings'))