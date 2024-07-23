# controllers/animal_controller.py
# Controlador para manejar la lógica relacionada con los animales

from models.animal import Animal
from models.purchase import Purchase
from models.request import Request
from persistence.database import Database
from persistence.json_persistence import JSONPersistence

class AnimalController:
    def __init__(self, db: Database, json_db: JSONPersistence = None):
        """
        Inicializa el controlador de animales con la conexión a la base de datos y opcionalmente la persistencia en JSON.
        :param db: Conexión a la base de datos
        :param json_db: (Opcional) Persistencia en JSON
        """
        self.db = db
        self.json_db = json_db

    def get_all_animals(self):
        """
        Obtiene todos los animales del inventario.
        :return: Lista de diccionarios con los datos de los animales
        """
        animals = Animal.get_all(self.db)
        return [animal.to_dict() for animal in animals]

    def buy_animal(self, user_id, animal_name, quantity):
        """
        Permite comprar un animal.
        :param user_id: ID del usuario que realiza la compra
        :param animal_name: Nombre del animal a comprar
        :param quantity: Cantidad a comprar
        :return: Diccionario con el resultado de la compra
        """
        animal = Animal.find_by_name(self.db, animal_name)
        if animal and animal.quantity >= quantity:
            animal.quantity -= quantity
            animal.save(self.db, self.json_db)
            purchase = Purchase(user_id, animal_name, quantity)
            purchase.save(self.db, self.json_db)
            return {"success": True, "message": "Compra realizada con éxito."}
        return {"success": False, "message": "Cantidad no disponible."}

    def request_animal(self, user_id, animal_name, phone):
        """
        Permite solicitar un animal que no está disponible en la tienda.
        :param user_id: ID del usuario que realiza la solicitud
        :param animal_name: Nombre del animal solicitado
        :param phone: Número de teléfono del usuario
        :return: Diccionario con el resultado de la solicitud
        """
        request = Request(user_id, animal_name, phone)
        request.save(self.db, self.json_db)
        return {"success": True, "message": "Solicitud registrada con éxito."}
