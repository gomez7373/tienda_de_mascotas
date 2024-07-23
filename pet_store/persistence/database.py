# persistence/database.py
# Maneja la conexión y operaciones con la base de datos SQLite

import sqlite3

class Database:
    def __init__(self, db_path=":memory:"):
        """
        Inicializa la conexión a la base de datos SQLite.
        :param db_path: Ruta del archivo de base de datos SQLite
        """
        self.connection = sqlite3.connect(db_path, check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        """
        Crea las tablas necesarias en la base de datos si no existen.
        """
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            name TEXT NOT NULL,
            surname TEXT NOT NULL,
            is_admin BOOLEAN NOT NULL DEFAULT 0
        )
        """)
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS animals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            quantity INTEGER NOT NULL
        )
        """)
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS purchases (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            animal TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
        """)
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS requests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            animal TEXT NOT NULL,
            phone TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
        """)
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS payments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            amount REAL NOT NULL,
            payment_date TEXT NOT NULL,
            payment_status TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
        """)
        self.connection.commit()

    def close(self):
        """
        Cierra la conexión a la base de datos.
        """
        self.connection.close()
