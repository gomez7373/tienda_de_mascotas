# routes/animal_routes.py
# Define las rutas para manejar las operaciones relacionadas con los animales

from flask import Blueprint, request, jsonify, render_template
from controllers.animal_controller import AnimalController
from persistence.database import Database
from persistence.json_persistence import JSONPersistence

animal_bp = Blueprint('animal_bp', __name__)

db = Database()
json_db = JSONPersistence()
animal_controller = AnimalController(db, json_db)

@animal_bp.route('/inventory', methods=['GET'])
def show_inventory():
    """
    Ruta para mostrar el inventario de animales.
    """
    animals = animal_controller.get_all_animals()
    return render_template('inventory.html', animals=animals)

@animal_bp.route('/buy', methods=['POST'])
def buy_animal():
    """
    Ruta para comprar un animal.
    Espera un JSON con los campos user_id, animal y quantity.
    """
    data = request.json
    user_id = data['user_id']
    animal = data['animal']
    quantity = data['quantity']
    response = animal_controller.buy_animal(user_id, animal, quantity)
    return jsonify(response), 200

@animal_bp.route('/request', methods=['GET', 'POST'])
def request_animal():
    """
    Ruta para solicitar un animal que no está disponible en la tienda.
    """
    if request.method == 'POST':
        data = request.form
        user_id = data['user_id']
        animal_name = data['animal_name']
        phone = data['phone']
        response = animal_controller.request_animal(user_id, animal_name, phone)
        return jsonify(response), 201
    return render_template('request.html')

@animal_bp.route('/history', methods=['GET'])
def get_purchase_history():
    """
    Ruta para obtener el historial de compras.
    """
    user_id = request.args.get('user_id')
    history = animal_controller.get_purchase_history(user_id)
    return jsonify(history), 200
