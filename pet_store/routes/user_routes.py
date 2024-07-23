# routes/user_routes.py
# Define las rutas para manejar las operaciones relacionadas con los usuarios

from flask import Blueprint, request, jsonify  # Importa Blueprint, request y jsonify de Flask
from controllers.user_controller import UserController  # Importa el controlador de usuarios
from persistence.database import Database  # Importa la clase Database
from persistence.json_persistence import JSONPersistence  # Importa la clase JSONPersistence

# Crear un Blueprint para las rutas de usuarios
user_bp = Blueprint('user_bp', __name__)

# Instanciar la base de datos y el controlador de usuarios
db = Database()
json_db = JSONPersistence()
user_controller = UserController(db, json_db)

@user_bp.route('/register', methods=['POST'])
def register():
    """
    Ruta para registrar un nuevo usuario.
    Espera un JSON con los campos email, password, name y surname.
    """
    data = request.json  # Obtener los datos JSON del request
    email = data['email']
    password = data['password']
    name = data['name']
    surname = data['surname']
    user = user_controller.create_user(email, password, name, surname)  # Crear el usuario
    return jsonify(user), 201  # Devolver el usuario creado y el código de estado 201 (Creado)

@user_bp.route('/login', methods=['POST'])
def login():
    """
    Ruta para autenticar un usuario.
    Espera un JSON con los campos email y password.
    """
    data = request.json  # Obtener los datos JSON del request
    email = data['email']
    password = data['password']
    user = user_controller.authenticate_user(email, password)  # Autenticar el usuario
    if user:
        return jsonify(user), 200  # Devolver el usuario autenticado y el código de estado 200 (OK)
    return jsonify({"error": "Autenticación fallida"}), 401  # Devolver un error y el código de estado 401 (No autorizado)

@user_bp.route('/check-admin', methods=['POST'])
def check_admin():
    """
    Ruta para verificar si un usuario es administrador.
    Espera un JSON con el campo email.
    """
    data = request.json  # Obtener los datos JSON del request
    email = data['email']
    is_admin = user_controller.check_admin(email)  # Verificar si el usuario es administrador
    return jsonify({"is_admin": is_admin}), 200  # Devolver el resultado y el código de estado 200 (OK)
