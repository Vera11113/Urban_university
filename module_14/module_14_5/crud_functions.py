import sqlite3


connection = sqlite3.connect('products.db')
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Products(
id INTEGER PRIMARY KEY,
title TEXT NOT NULL,
description TEXT,
price INTEGER NOT NULL
)
"""
)

# for i in range(1, 5):
#   cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)", (f'Продукт{i}', f'Описание{i}', i*100))



# cursor.execute("SELECT * FROM Products")
# products = cursor.fetchmany(4)
# # print(products)

connection.commit()
connection.close()


class Users:

    def __init__(self):
        self.connection = sqlite3.connect('Users.db')
        self.cursor = self.connection.cursor()

    def initiate_db(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INT NOT NULL,
        balance INT NOT NULL
        )
        """)
        self.connection.commit()

    def add_user(self, username, email, age):
        self.cursor.execute("INSERT INTO Users(username, email, age, balance) VALUES(?, ?, ?, ?)", (username, email, age, 1000))
        self.connection.commit()

    def is_included(self, username):
        user = self.cursor.execute("SELECT username FROM Users WHERE username = ?", (username,)).fetchone()
        if user is None:
            return True
        else: return  False

    def delete(self, user):
        self.cursor.execute('DELETE FROM Users WHERE username = ?', (user, ))
        self.connection.commit()

    def close(self):
        self.connection.commit()
        self.connection.close()
