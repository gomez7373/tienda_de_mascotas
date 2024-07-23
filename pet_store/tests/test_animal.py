# tests/test_animal.py
# Archivo de pruebas para la funcionalidad del controlador de animales

import unittest  # Importa el módulo unittest para realizar las pruebas
from models.animal import Animal  # Importa la clase Animal desde el módulo models.animal
from controllers.animal_controller import AnimalController  # Importa el controlador de animales
from persistence.database import Database  # Importa la clase Database
from persistence.json_persistence import JSONPersistence  # Importa la clase JSONPersistence

class TestAnimalController(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        Configuración inicial antes de ejecutar cualquier prueba.
        """
        cls.db = Database(":memory:")  # Crea una base de datos en memoria para las pruebas
        cls.json_db = JSONPersistence("test_data.json")  # Crea un archivo JSON temporal para las pruebas
        cls.animal_controller = AnimalController(cls.db, cls.json_db)  # Crea una instancia del controlador de animales

    def test_add_animal(self):
        """
        Prueba la adición de un nuevo animal.
        """
        animal_data = {
            "name": "perro",
            "quantity": 10
        }
        animal = self.animal_controller.add_animal(**animal_data)
        self.assertEqual(animal["name"], animal_data["name"])
        self.assertEqual(animal["quantity"], animal_data["quantity"])

    def test_buy_animal(self):
        """
        Prueba la compra de un animal.
        """
        user_id = 1
        animal_name = "perro"
        quantity = 2
        self.animal_controller.add_animal(animal_name, 10)
        response, status = self.animal_controller.buy_animal(user_id, animal_name, quantity)
        self.assertEqual(status, 200)
        self.assertEqual(response["purchase"]["animal"], animal_name)
        self.assertEqual(response["purchase"]["quantity"], quantity)
        self.assertEqual(response["new_inventory"]["quantity"], 8)

    def test_request_animal(self):
        """
        Prueba la solicitud de un animal no disponible.
        """
        user_id = 1
        animal_name = "camaleón"
        phone = "1234567890"
        request = self.animal_controller.request_animal(user_id, animal_name, phone)
        self.assertEqual(request["animal"], animal_name)
        self.assertEqual(request["phone"], phone)

    def test_get_animals(self):
        """
        Prueba la obtención de todos los animales disponibles en la tienda.
        """
        self.animal_controller.add_animal("gato", 5)
        animals = self.animal_controller.get_animals()
        self.assertIn("gato", animals)
        self.assertEqual(animals["gato"], 5)

    @classmethod
    def tearDownClass(cls):
        """
        Limpieza después de ejecutar todas las pruebas.
        """
        cls.db.close()  # Cierra la conexión a la base de datos
        import os
        os.remove("test_data.json")  # Elimina el archivo JSON temporal

if __name__ == "__main__":
    unittest.main()
