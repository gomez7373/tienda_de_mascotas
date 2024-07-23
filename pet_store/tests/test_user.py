# tests/test_user.py
# Archivo de pruebas para la funcionalidad del controlador de usuarios

import unittest  # Importa el módulo unittest para realizar las pruebas
from models.user import User  # Importa la clase User desde el módulo models.user
from controllers.user_controller import UserController  # Importa el controlador de usuarios
from persistence.database import Database  # Importa la clase Database
from persistence.json_persistence import JSONPersistence  # Importa la clase JSONPersistence
from base import hash_password  # Importa la función hash_password

class TestUserController(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        Configuración inicial antes de ejecutar cualquier prueba.
        """
        cls.db = Database(":memory:")  # Crea una base de datos en memoria para las pruebas
        cls.json_db = JSONPersistence("test_data.json")  # Crea un archivo JSON temporal para las pruebas
        cls.user_controller = UserController(cls.db, cls.json_db)  # Crea una instancia del controlador de usuarios

    def test_create_user(self):
        """
        Prueba la creación de un nuevo usuario.
        """
        user_data = {
            "email": "test@example.com",
            "password": "Test1234!",
            "name": "John",
            "surname": "Doe"
        }
        user = self.user_controller.create_user(**user_data)
        self.assertEqual(user["email"], user_data["email"])
        self.assertTrue("password" not in user)  # Asegúrate de que la contraseña no esté en el diccionario devuelto

    def test_authenticate_user(self):
        """
        Prueba la autenticación de un usuario.
        """
        email = "test@example.com"
        password = "Test1234!"
        user = self.user_controller.authenticate_user(email, password)
        self.assertIsNotNone(user)
        self.assertEqual(user["email"], email)

    def test_check_admin(self):
        """
        Prueba la verificación de administrador de un usuario.
        """
        email = "admin@example.com"
        self.user_controller.create_user(email, "Admin1234!", "Admin", "User", is_admin=True)
        self.assertTrue(self.user_controller.check_admin(email))

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
