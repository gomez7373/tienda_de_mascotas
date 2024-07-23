# persistence/json_persistence.py
# Maneja la persistencia de datos en archivos JSON

import json  # Importa el módulo json para trabajar con datos en formato JSON
import os  # Importa el módulo os para interactuar con el sistema operativo

class JSONPersistence:
    def __init__(self, filepath="data.json"):
        """
        Inicializa la persistencia en JSON.
        :param filepath: Ruta del archivo JSON
        """
        self.filepath = filepath  # Almacena la ruta del archivo JSON
        if not os.path.exists(filepath):  # Verifica si el archivo JSON no existe
            with open(filepath, 'w') as file:
                # Crea el archivo JSON con una estructura inicial
                json.dump({"users": [], "animals": [], "purchases": [], "requests": [], "payments": []}, file)

    def read(self):
        """
        Lee los datos del archivo JSON.
        :return: Diccionario con los datos leídos del archivo JSON
        """
        with open(self.filepath, 'r') as file:
            return json.load(file)  # Leer y devolver los datos del archivo JSON

    def write(self, data):
        """
        Escribe los datos en el archivo JSON.
        :param data: Diccionario con los datos a escribir en el archivo JSON
        """
        with open(self.filepath, 'w') as file:
            json.dump(data, file, indent=4)  # Escribir los datos en el archivo JSON con indentación

    def append(self, section, item):
        """
        Añade un elemento a una sección específica en el archivo JSON.
        :param section: Sección del archivo JSON donde se añadirá el elemento (ej. 'users', 'animals')
        :param item: Diccionario con los datos del elemento a añadir
        """
        data = self.read()  # Leer los datos actuales del archivo JSON
        data[section].append(item)  # Añadir el nuevo elemento a la sección correspondiente
        self.write(data)  # Escribir los datos actualizados en el archivo JSON
