import os
"""
 Genera una clave secreta (SECRET_KEY) segura para la aplicación Flask,
 esta crear una clave aleatoria. 
"""
# Genera una clave secreta de 24 bytes
secret_key = os.urandom(24)
print(secret_key.hex())

