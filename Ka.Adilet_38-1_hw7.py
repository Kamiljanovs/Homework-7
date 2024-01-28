import sqlite3

def create_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return connection

def create_table(connection, sql):
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)

def add_product(connection, product):
    sql = '''INSERT INTO products 
    (product_title , price , quantity)
    VALUES 
    (?, ?, ?)'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, product)
        connection.commit()
    except sqlite3.Error as e:
        print(e)


def update_product(connection, product):
    sql = '''UPDATE products SET quantity = ?, price = ? 
                WHERE id = ?'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, product)
        connection.commit()
    except sqlite3.Error as e:
        print(e)

def delete_product(connection, id):
    sql = '''DELETE FROM products WHERE id = ?'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, (id,))
        connection.commit()
    except sqlite3.Error as e:
        print(e)

def select_all_products(connection):
    sql = '''SELECT * FROM products'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
        rows_list = cursor.fetchall()

        for row in rows_list:
            print(row)
    except sqlite3.Error as e:
        print(e)


def select_products_by_limits(connection):
    sql = '''SELECT * FROM products WHERE price < 100 AND quantity > 15'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
        rows_list = cursor.fetchall()

        for row in rows_list:
            print(row)
    except sqlite3.Error as e:
        print(e)


def search_by_title(connection):
    sql = '''SELECT * FROM products WHERE product_title LIKE ('%мыло%') '''
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
        rows_list = cursor.fetchall()

        for row in rows_list:
            print(row)
    except sqlite3.Error as e:
        print(e)



create_product_table = '''
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title TEXT NOT NULL,
    price REAL DEFAULT 0.0 NOT NULL,
    quantity INTEGER DEFAULT 0 NOT NULL
)
'''


my_connection = create_connection('hw.db')
if my_connection is not None:
     print('Successfully connected to DB!')
     # create_table(my_connection, create_product_table)
     # add_product(my_connection, ('Хозяйтсвенное мыло', 30, 35))
     # add_product(my_connection, ('Жидкое мыло', 50, 20))
     # add_product(my_connection, ('Детское мыло', 40, 25))
     # add_product(my_connection, ('Автомат порошок', 80, 15))
     # add_product(my_connection, ('Ручной порошок', 60, 20))
     # add_product(my_connection, ('Молоко', 75, 40))
     # add_product(my_connection, ('Домашнее молоко', 80, 20))
     # add_product(my_connection, ('Растительное масло', 100, 15))
     # add_product(my_connection, ('Беловодское масло', 100, 15))
     # add_product(my_connection, ('Хлеб лепешка', 28, 60))
     # add_product(my_connection, ('Хлеб булка', 33, 55))
     # add_product(my_connection, ('Мужской шампунь', 120, 25))
     # add_product(my_connection, ('Женский шампунь', 150, 30))
     # add_product(my_connection, ('Детский шампунь', 100, 15))
     # add_product(my_connection, ('Кефир', 65, 35))
     # update_product(my_connection, (40, 80, 15))
     # delete_product(my_connection, 10)
     # select_all_products(my_connection)
     # select_products_by_limits(my_connection)
     # search_by_title(my_connection)
     my_connection.close()



