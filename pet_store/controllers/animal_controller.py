# controllers/animal_controller.py
# Controlador para manejar la lógica relacionada con los animales

from models.animal import Animal  # Importa la clase Animal desde el módulo models.animal
from models.purchase import Purchase  # Importa la clase Purchase desde el módulo models.purchase
from models.request import Request  # Importa la clase Request desde el módulo models.request
from persistence.database import Database  # Importa la clase Database desde el módulo persistence.database
from persistence.json_persistence import JSONPersistence  # Importa la clase JSONPersistence desde el módulo persistence.json_persistence
from datetime import datetime  # Importa el módulo datetime para manejar fechas

class AnimalController:
    def __init__(self, db: Database, json_db: JSONPersistence = None):
        """
        Inicializa el controlador de animales con la conexión a la base de datos y opcionalmente la persistencia en JSON.
        :param db: Conexión a la base de datos
        :param json_db: (Opcional) Persistencia en JSON
        """
        self.db = db  # Almacena la conexión a la base de datos
        self.json_db = json_db  # Almacena la persistencia en JSON si se proporciona

    def add_animal(self, name, quantity):
        """
        Agrega un nuevo animal a la base de datos.
        :param name: Nombre del animal
        :param quantity: Cantidad de animales disponibles
        :return: Diccionario con los datos del animal agregado
        """
        animal = Animal(name, quantity)  # Crea una nueva instancia de Animal
        animal.save(self.db, self.json_db)  # Guarda el animal en la base de datos (y en JSON si se proporciona)
        return animal.to_dict()  # Devuelve un diccionario con los datos del animal agregado

    def buy_animal(self, user_id, animal_name, quantity):
        """
        Realiza la compra de un animal, actualizando la cantidad disponible.
        :param user_id: ID del usuario que compra el animal
        :param animal_name: Nombre del animal comprado
        :param quantity: Cantidad de animales comprados
        :return: Diccionario con los detalles de la compra y el nuevo estado del inventario
        """
        # Obtiene la cantidad actual del animal en la base de datos
        current_animals = Animal.get_all(self.db)
        if animal_name in current_animals:
            current_quantity = current_animals[animal_name]
            if current_quantity >= quantity:  # Verifica si hay suficiente cantidad disponible
                new_quantity = current_quantity - quantity  # Calcula la nueva cantidad
                animal = Animal(animal_name, new_quantity)
                animal.update_quantity(self.db, new_quantity, self.json_db)  # Actualiza la cantidad en la base de datos
                purchase = Purchase(user_id, animal_name, quantity, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                purchase.save(self.db, self.json_db)  # Guarda la compra en la base de datos
                return {"purchase": purchase.to_dict(), "new_inventory": animal.to_dict()}, 200
            else:
                return {"error": "Cantidad insuficiente en el inventario."}, 400
        return {"error": "Animal no encontrado en el inventario."}, 404

    def request_animal(self, user_id, animal_name, phone):
        """
        Realiza una solicitud para un animal no disponible actualmente.
        :param user_id: ID del usuario que solicita el animal
        :param animal_name: Nombre del animal solicitado
        :param phone: Número de teléfono del usuario para contacto
        :return: Diccionario con los datos de la solicitud
        """
        request = Request(user_id, animal_name, phone)  # Crea una nueva instancia de Request
        request.save(self.db, self.json_db)  # Guarda la solicitud en la base de datos (y en JSON si se proporciona)
        return request.to_dict()  # Devuelve un diccionario con los datos de la solicitud

    def get_animals(self):
        """
        Obtiene todos los animales disponibles en la tienda.
        :return: Diccionario con todos los animales y sus cantidades
        """
        return Animal.get_all(self.db)  # Devuelve un diccionario con todos los animales y sus cantidades

    def get_purchase_history(self, user_id):
        """
        Obtiene el historial de compras de un usuario específico.
        :param user_id: ID del usuario
        :return: Lista de diccionarios con los detalles de las compras del usuario
        """
        purchases = Purchase.get_by_user(self.db, user_id)  # Obtiene todas las compras del usuario
        return [dict(purchase) for purchase in purchases]  # Devuelve una lista de diccionarios con los detalles de las compras
