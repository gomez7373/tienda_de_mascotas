# models/animal.py
# Define el modelo de datos para los animales

from persistence.json_persistence import JSONPersistence  # Importa la clase JSONPersistence para la persistencia en archivos JSON

class Animal:
    def __init__(self, name, quantity):
        """
        Inicializa un nuevo animal con los detalles proporcionados.
        :param name: Nombre del animal
        :param quantity: Cantidad disponible del animal
        """
        self.name = name  # Almacena el nombre del animal
        self.quantity = quantity  # Almacena la cantidad disponible del animal

    def save(self, db, json_db=None):
        """
        Guarda el animal en la base de datos.
        :param db: Conexión a la base de datos
        :param json_db: (Opcional) Persistencia en JSON
        """
        db.cursor.execute("INSERT INTO animals (name, quantity) VALUES (?, ?)", (self.name, self.quantity))
        db.connection.commit()  # Guardar cambios en la base de datos
        if json_db:
            json_db.append("animals", self.to_dict())  # Guardar en JSON si se proporciona

    def update_quantity(self, db, new_quantity, json_db=None):
        """
        Actualiza la cantidad del animal en la base de datos.
        :param db: Conexión a la base de datos
        :param new_quantity: Nueva cantidad del animal
        :param json_db: (Opcional) Persistencia en JSON
        """
        db.cursor.execute("UPDATE animals SET quantity = ? WHERE name = ?", (new_quantity, self.name))
        db.connection.commit()  # Guardar cambios en la base de datos
        if json_db:
            data = json_db.read()
            for animal in data['animals']:
                if animal['name'] == self.name:
                    animal['quantity'] = new_quantity
                    break
            json_db.write(data)  # Guardar cambios en el archivo JSON

    @staticmethod
    def get_all(db):
        """
        Obtiene todos los animales de la base de datos.
        :param db: Conexión a la base de datos
        :return: Diccionario con todos los animales y sus cantidades
        """
        db.cursor.execute("SELECT name, quantity FROM animals")
        animals = db.cursor.fetchall()  # Obtener todos los animales
        return {name: quantity for name, quantity in animals}

    def to_dict(self):
        """
        Convierte el objeto Animal a un diccionario.
        :return: Diccionario con los datos del animal
        """
        return {
            "name": self.name,  # Nombre del animal
            "quantity": self.quantity  # Cantidad disponible del animal
        }
