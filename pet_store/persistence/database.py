# persistence/database.py
# Maneja la conexión y operaciones con la base de datos SQLite

import sqlite3  # Importa el módulo sqlite3 para interactuar con bases de datos SQLite

class Database:
    def __init__(self, db_name="pet_store.db"):
        """
        Inicializa la conexión a la base de datos SQLite.
        :param db_name: Nombre del archivo de la base de datos
        """
        self.connection = sqlite3.connect(db_name)  # Establecer conexión con la base de datos SQLite
        self.cursor = self.connection.cursor()  # Crear un cursor para ejecutar comandos SQL
        self.create_tables()  # Crear las tablas si no existen

    def create_tables(self):
        """
        Crea las tablas necesarias en la base de datos si no existen.
        """
        # Crear tabla de animales
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS animals (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            quantity INTEGER NOT NULL
        )
        """)
        # Crear tabla de usuarios
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            email TEXT NOT NULL,
            password TEXT NOT NULL,
            name TEXT NOT NULL,
            surname TEXT NOT NULL,
            is_admin INTEGER NOT NULL
        )
        """)
        # Crear tabla de solicitudes
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS requests (
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            animal TEXT NOT NULL,
            phone TEXT NOT NULL,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
        """)
        # Crear tabla de compras
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS purchases (
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            animal TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            purchase_date TEXT NOT NULL,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
        """)
        # Crear tabla de pagos
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS payments (
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            amount REAL NOT NULL,
            payment_date TEXT NOT NULL,
            payment_status TEXT NOT NULL,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
        """)
        self.connection.commit()  # Guardar los cambios en la base de datos

    def close(self):
        """
        Cierra la conexión a la base de datos.
        """
        self.connection.close()  # Cerrar la conexión
