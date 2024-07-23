pet_store/
│
├── .env                   # Archivo para almacenar variables de entorno (no debe estar en el repositorio)
├── .gitignore              # Archivo que indica qué archivos/directorios deben ser ignorados por Git
├── app.py                 # Archivo principal para inicializar y ejecutar la aplicación Flask
├── base.py                # Archivo base con funciones comunes utilizadas en otros archivos
├── config.py              # Archivo para la configuración de la aplicación (puede incluir configuraciones de Flask, base de datos, etc.)
│
├── controllers/           # Directorio que contiene los controladores que manejan la lógica de negocio
│   ├── user_controller.py # Controlador para manejar la lógica relacionada con los usuarios (registro, autenticación, etc.)
│   └── animal_controller.py # Controlador para manejar la lógica relacionada con los animales (compras, adiciones, solicitudes, etc.)
│
├── models/                # Directorio que contiene los modelos de datos y clases para la base de datos
│   ├── user.py            # Modelo para el usuario, define las operaciones y la estructura de los datos del usuario
│   ├── animal.py          # Modelo para el animal, define las operaciones y la estructura de los datos del animal
│   ├── purchase.py        # Modelo para la compra, define las operaciones y la estructura de los datos de las compras
│   ├── request.py         # Modelo para las solicitudes de animales, define las operaciones y la estructura de los datos de las solicitudes
│   └── payment.py         # Modelo para los pagos, define las operaciones y la estructura de los datos de los pagos
│
├── persistence/           # Directorio para la lógica de persistencia de datos
│   ├── database.py        # Maneja la conexión y operaciones con la base de datos SQLite
│   └── json_persistence.py # Maneja la persistencia de datos en archivos JSON
│
├── routes/                # Directorio que contiene las rutas de la aplicación
│   ├── user_routes.py     # Define las rutas relacionadas con las operaciones de usuario
│   └── animal_routes.py   # Define las rutas relacionadas con las operaciones de animales
│
├── static/                # Directorio para archivos estáticos (CSS, JavaScript, imágenes)
│   ├── css/               # Directorio para archivos CSS
│   ├── js/                # Directorio para archivos JavaScript
│   └── images/            # Directorio para imágenes
│
├── tests/                 # Directorio para los archivos de prueba
│   ├── test_user.py       # Pruebas para la funcionalidad del controlador de usuarios
│   ├── test_animal.py     # Pruebas para la funcionalidad del controlador de animales
│   ├── test_purchase.py   # Pruebas para la funcionalidad del modelo de compras
│   └── test_request.py    # Pruebas para la funcionalidad del modelo de solicitudes
│
├── tienda.py              # Archivo de entrada para la aplicación (puede contener la lógica principal o inicialización)
├── templates/            # Directorio para las plantillas HTML
│   ├── index.html         # Plantilla para la página principal
│   ├── purchase.html      # Plantilla para la página de compra
│   └── payment.html       # Plantilla para la página de pago
│
├── README.md              # Archivo de documentación del proyecto
└── requirements.txt       # Archivo que lista las dependencias del proyecto

