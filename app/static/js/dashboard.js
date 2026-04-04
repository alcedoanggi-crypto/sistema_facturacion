document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('productSearch');
    const productRows = document.querySelectorAll('.product-row');
    const totalDisplay = document.getElementById('invoice-total-display'); // Necesitaremos este ID en el HTML

    // --- 1. Lógica de Búsqueda ---
    if (searchInput) {
        searchInput.addEventListener('keyup', function() {
            const filter = this.value.toLowerCase();
            productRows.forEach(row => {
                const productName = row.querySelector('.product-name').textContent.toLowerCase();
                row.style.display = productName.includes(filter) ? "" : "none";
            });
        });
    }

    // --- 2. Lógica de Selección y Cantidad ---
    document.querySelectorAll('.product-check').forEach(checkbox => {
        checkbox.addEventListener('change', function() {
            const row = this.closest('tr');
            const qtyInput = row.querySelector('.quantity-input');

            if (this.checked) {
                qtyInput.disabled = false;
                if (qtyInput.value <= 0) qtyInput.value = 1;
                row.classList.add('table-primary');
            } else {
                qtyInput.disabled = true;
                qtyInput.value = 0;
                row.classList.remove('table-primary');
            }
            calculateTotal(); // Recalcular cuando cambie la selección
        });
    });

    // --- 3. Lógica para recalcular cuando cambie la cantidad manualmente ---
    document.querySelectorAll('.quantity-input').forEach(input => {
        input.addEventListener('input', calculateTotal);
    });

    // --- 4. Función para calcular el Total ---
    function calculateTotal() {
        let subtotal = 0;
        document.querySelectorAll('.product-row').forEach(row => {
            const checkbox = row.querySelector('.product-check');
            if (checkbox.checked) {
                const priceText = row.cells[2].textContent.replace('$', '').replace(',', '');
                const price = parseFloat(priceText);
                const quantity = parseInt(row.querySelector('.quantity-input').value) || 0;
                subtotal += price * quantity;
            }
        });

        if (totalDisplay) {
            const tax = subtotal * 0.19; // IVA 19%
            const total = subtotal + tax;
            totalDisplay.innerHTML = `
                <div class="text-end">
                    <p>Subtotal: $${subtotal.toLocaleString()}</p>
                    <p>IVA (19%): $${tax.toLocaleString()}</p>
                    <h4 class="text-success">Total: $${total.toLocaleString()}</h4>
                </div>
            `;
        }
    }
});

// Asegúrate de que este código esté en tu archivo .js externo

document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('reportSearch');
    if (searchInput) {
        searchInput.addEventListener('keyup', function() {
            const query = this.value.toLowerCase();
            const rows = document.querySelectorAll('#salesTable tbody tr');

            rows.forEach(row => {
                // Esto busca en toda la fila (ID, Cliente y Fecha)
                const text = row.innerText.toLowerCase();
                row.style.display = text.includes(query) ? '' : 'none';
            });
        });
    }
});