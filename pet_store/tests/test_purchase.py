# tests/test_purchase.py
# Archivo de pruebas para la funcionalidad del modelo de compras

import unittest  # Importa el módulo unittest para realizar las pruebas
from models.purchase import Purchase  # Importa la clase Purchase desde el módulo models.purchase
from persistence.database import Database  # Importa la clase Database
from persistence.json_persistence import JSONPersistence  # Importa la clase JSONPersistence
from datetime import datetime  # Importa el módulo datetime para manejar fechas

class TestPurchaseModel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        Configuración inicial antes de ejecutar cualquier prueba.
        """
        cls.db = Database(":memory:")  # Crea una base de datos en memoria para las pruebas
        cls.json_db = JSONPersistence("test_data.json")  # Crea un archivo JSON temporal para las pruebas

    def test_create_purchase(self):
        """
        Prueba la creación de una nueva compra.
        """
        user_id = 1
        animal = "perro"
        quantity = 2
        purchase_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        purchase = Purchase(user_id, animal, quantity, purchase_date)
        purchase.save(self.db, self.json_db)
        
        self.db.cursor.execute("SELECT * FROM purchases WHERE user_id = ? AND animal = ?", (user_id, animal))
        result = self.db.cursor.fetchone()
        
        self.assertIsNotNone(result)
        self.assertEqual(result[1], user_id)
        self.assertEqual(result[2], animal)
        self.assertEqual(result[3], quantity)

    def test_get_purchases_by_user(self):
        """
        Prueba la obtención de todas las compras de un usuario específico.
        """
        user_id = 1
        purchases = Purchase.get_by_user(self.db, user_id)
        self.assertIsInstance(purchases, list)

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
