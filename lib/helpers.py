import sqlite3
from models.product import create_connection

def add_product(name, quantity, supplier):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT id FROM suppliers WHERE name = ?', (supplier,))
    supplier_id = cursor.fetchone()
    if not supplier_id:
        cursor.execute('INSERT INTO suppliers (name) VALUES (?)', (supplier,))
        supplier_id = cursor.lastrowid
    else:
        supplier_id = supplier_id[0]

    cursor.execute('''
        INSERT INTO products (name, quantity, remaining_quantity, supplier_id)
        VALUES (?, ?, ?, ?)
    ''', (name, quantity, quantity, supplier_id))

    conn.commit()
    conn.close()
    print(f'Added product {name} with quantity {quantity} from supplier {supplier}.')

def view_products():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT p.id, p.name, p.quantity, p.quantity_sold, p.remaining_quantity, s.name
        FROM products p
        JOIN suppliers s ON p.supplier_id = s.id
    ''')
    products = cursor.fetchall()
    conn.close()
    
    if not products:
        print('No products found.')
    else:
        for product in products:
            print(f'{product[0]}: {product[1]} - {product[2]} quantity - {product[3]} sold - {product[4]} remaining - Supplier: {product[5]}')

def update_product(id, name, quantity, quantity_sold, supplier):
    conn = create_connection()
    cursor = conn.cursor()

    if name:
        cursor.execute('UPDATE products SET name = ? WHERE id = ?', (name, id))
    if quantity is not None:
        cursor.execute('UPDATE products SET quantity = ?, remaining_quantity = ? - quantity_sold WHERE id = ?', (quantity, quantity, id))
    if quantity_sold is not None:
        cursor.execute('UPDATE products SET quantity_sold = ?, remaining_quantity = quantity - ? WHERE id = ?', (quantity_sold, quantity_sold, id))
    if supplier:
        cursor.execute('SELECT id FROM suppliers WHERE name = ?', (supplier,))
        supplier_id = cursor.fetchone()
        if not supplier_id:
            cursor.execute('INSERT INTO suppliers (name) VALUES (?)', (supplier,))
            supplier_id = cursor.lastrowid
        else:
            supplier_id = supplier_id[0]
        cursor.execute('UPDATE products SET supplier_id = ? WHERE id = ?', (supplier_id, id))

    conn.commit()
    conn.close()
    print(f'Updated product {id}.')

def view_suppliers():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id, name FROM suppliers')
    suppliers = cursor.fetchall()
    conn.close()

    if not suppliers:
        print('No suppliers found.')
    else:
        for supplier in suppliers:
            print(f'{supplier[0]}: {supplier[1]}')
