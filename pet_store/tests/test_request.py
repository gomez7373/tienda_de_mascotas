# tests/test_request.py
# Archivo de pruebas para la funcionalidad del modelo de solicitudes

import unittest  # Importa el módulo unittest para realizar las pruebas
from models.request import Request  # Importa la clase Request desde el módulo models.request
from persistence.database import Database  # Importa la clase Database
from persistence.json_persistence import JSONPersistence  # Importa la clase JSONPersistence

class TestRequestModel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        Configuración inicial antes de ejecutar cualquier prueba.
        """
        cls.db = Database(":memory:")  # Crea una base de datos en memoria para las pruebas
        cls.json_db = JSONPersistence("test_data.json")  # Crea un archivo JSON temporal para las pruebas

    def test_create_request(self):
        """
        Prueba la creación de una nueva solicitud.
        """
        user_id = 1
        animal = "camaleón"
        phone = "1234567890"
        request = Request(user_id, animal, phone)
        request.save(self.db, self.json_db)
        
        self.db.cursor.execute("SELECT * FROM requests WHERE user_id = ? AND animal = ?", (user_id, animal))
        result = self.db.cursor.fetchone()
        
        self.assertIsNotNone(result)
        self.assertEqual(result[1], user_id)
        self.assertEqual(result[2], animal)
        self.assertEqual(result[3], phone)

    def test_get_requests_by_user(self):
        """
        Prueba la obtención de todas las solicitudes de un usuario específico.
        """
        user_id = 1
        requests = Request.get_by_user(self.db, user_id)
        self.assertIsInstance(requests, list)

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
