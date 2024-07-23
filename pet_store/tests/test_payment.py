# tests/test_payment.py
# Archivo de pruebas para la funcionalidad del modelo de pagos

import unittest  # Importa el módulo unittest para realizar las pruebas
from models.payment import Payment  # Importa la clase Payment desde el módulo models.payment
from persistence.database import Database  # Importa la clase Database
from persistence.json_persistence import JSONPersistence  # Importa la clase JSONPersistence
from datetime import datetime  # Importa el módulo datetime para manejar fechas

class TestPaymentModel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        Configuración inicial antes de ejecutar cualquier prueba.
        """
        cls.db = Database(":memory:")  # Crea una base de datos en memoria para las pruebas
        cls.json_db = JSONPersistence("test_data.json")  # Crea un archivo JSON temporal para las pruebas

    def test_create_payment(self):
        """
        Prueba la creación de un nuevo pago.
        """
        user_id = 1
        amount = 100.0
        payment_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        payment_status = "completado"
        payment = Payment(user_id, amount, payment_date, payment_status)
        payment.save(self.db, self.json_db)
        
        self.db.cursor.execute("SELECT * FROM payments WHERE user_id = ? AND amount = ?", (user_id, amount))
        result = self.db.cursor.fetchone()
        
        self.assertIsNotNone(result)
        self.assertEqual(result[1], user_id)
        self.assertEqual(result[2], amount)
        self.assertEqual(result[3], payment_date)
        self.assertEqual(result[4], payment_status)

    def test_get_payments_by_user(self):
        """
        Prueba la obtención de todos los pagos de un usuario específico.
        """
        user_id = 1
        payments = Payment.get_by_user(self.db, user_id)
        self.assertIsInstance(payments, list)

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
