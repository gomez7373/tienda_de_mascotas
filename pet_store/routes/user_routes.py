# routes/user_routes.py
# Define las rutas para manejar las operaciones relacionadas con los usuarios

from flask import Blueprint, request, jsonify, render_template, redirect, url_for, session
from controllers.user_controller import UserController
from persistence.database import Database
from persistence.json_persistence import JSONPersistence

user_bp = Blueprint('user_bp', __name__)

db = Database()
json_db = JSONPersistence()
user_controller = UserController(db, json_db)

@user_bp.route('/register', methods=['GET'])
def show_register():
    """
    Ruta para mostrar la página de registro.
    """
    return render_template('register.html')

@user_bp.route('/register', methods=['POST'])
def register_user():
    """
    Ruta para registrar un nuevo usuario.
    Espera un JSON con los campos email, password, name y surname.
    """
    data = request.json
    email = data['email']
    password = data['password']
    name = data['name']
    surname = data['surname']
    is_admin = data.get('is_admin', False)
    user_controller.create_user(email, password, name, surname, is_admin)
    return jsonify({"success": True}), 201

@user_bp.route('/login', methods=['GET'])
def show_login():
    """
    Ruta para mostrar la página de inicio de sesión.
    """
    return render_template('login.html')

@user_bp.route('/login', methods=['POST'])
def login_user():
    """
    Ruta para autenticar un usuario.
    Espera un JSON con los campos email y password.
    """
    data = request.json
    email = data['email']
    password = data['password']
    response = user_controller.authenticate_user(email, password)
    if response:
        # Guardar los detalles del usuario en la sesión
        session['user_id'] = response['id']
        session['user_email'] = response['email']
        session['user_name'] = response['name']
        session['user_surname'] = response['surname']
        session['is_admin'] = response['is_admin']
        return redirect(url_for('user_bp.menu'))
    return jsonify({"error": "Invalid credentials"}), 401

@user_bp.route('/menu', methods=['GET'])
def menu():
    """
    Ruta para mostrar el menú después de iniciar sesión.
    """
    if 'user_id' not in session:
        return redirect(url_for('user_bp.show_login'))
    return render_template('menu.html', user=session)
