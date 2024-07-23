# routes/animal_routes.py
# Define las rutas para manejar las operaciones relacionadas con los animales

from flask import Blueprint, request, jsonify  # Importa Blueprint, request y jsonify de Flask
from controllers.animal_controller import AnimalController  # Importa el controlador de animales
from persistence.database import Database  # Importa la clase Database
from persistence.json_persistence import JSONPersistence  # Importa la clase JSONPersistence

# Crear un Blueprint para las rutas de animales
animal_bp = Blueprint('animal_bp', __name__)

# Instanciar la base de datos y el controlador de animales
db = Database()
json_db = JSONPersistence()
animal_controller = AnimalController(db, json_db)

@animal_bp.route('/animals', methods=['GET'])
def get_animals():
    """
    Ruta para obtener la lista de animales en la tienda.
    """
    return jsonify(animal_controller.get_animals()), 200  # Devuelve la lista de animales y el código de estado 200 (OK)

@animal_bp.route('/buy', methods=['POST'])
def buy_animal():
    """
    Ruta para comprar un animal.
    Espera un JSON con los campos user_id, animal y quantity.
    """
    data = request.json  # Obtener los datos JSON del request
    user_id = data['user_id']
    response, status = animal_controller.buy_animal(user_id, data['animal'].lower(), data['quantity'])  # Realiza la compra del animal
    return jsonify(response), status  # Devuelve el resultado de la compra y el código de estado correspondiente

@animal_bp.route('/add', methods=['POST'])
def add_animal():
    """
    Ruta para agregar un nuevo animal a la tienda.
    Espera un JSON con los campos animal y quantity.
    """
    data = request.json  # Obtener los datos JSON del request
    response = animal_controller.add_animal(data['animal'].lower(), data['quantity'])  # Agrega el nuevo animal
    return jsonify(response), 200  # Devuelve el animal agregado y el código de estado 200 (OK)

@animal_bp.route('/request', methods=['POST'])
def request_animal():
    """
    Ruta para solicitar un animal no disponible actualmente.
    Espera un JSON con los campos user_id, animal y phone.
    """
    data = request.json  # Obtener los datos JSON del request
    response = animal_controller.request_animal(data['user_id'], data['animal'], data['phone'])  # Realiza la solicitud del animal
    return jsonify(response), 201  # Devuelve la solicitud realizada y el código de estado 201 (Creado)

@animal_bp.route('/purchase_history/<int:user_id>', methods=['GET'])
def get_purchase_history(user_id):
    """
    Ruta para obtener el historial de compras de un usuario específico.
    :param user_id: ID del usuario
    """
    return jsonify(animal_controller.get_purchase_history(user_id)), 200  # Devuelve el historial de compras del usuario y el código de estado 200 (OK)

@animal_bp.route('/pay', methods=['POST'])
def make_payment():
    """
    Ruta para realizar un pago.
    Espera un JSON con los campos user_id y amount.
    """
    data = request.json  # Obtener los datos JSON del request
    user_id = data['user_id']
    amount = data['amount']
    response = animal_controller.make_payment(user_id, amount)  # Realiza el pago
    return jsonify(response), 200  # Devuelve el resultado del pago y el código de estado 200 (OK)
