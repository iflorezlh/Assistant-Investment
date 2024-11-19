from src.database.db_connection import SqlConnection
import os
import json
import pandas as pd

# Ruta al archivo JSON
path = r'/home/ivanfl/Assistant-Investment/config/api_keys.json'

# Leer el archivo JSON y cargarlo como un diccionario
with open(path, 'r') as file:
    credenciales = json.load(file)

# Imprimir las credenciales
server = credenciales['bd_credentials']['server']
database = credenciales['bd_credentials']['database']
