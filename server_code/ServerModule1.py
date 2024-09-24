import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
import pandas as pd

@anvil.server.callable
def procesar_archivo(file):
    # Leer el archivo CSV desde el cliente
    df = pd.read_csv(file)
    
    # Convertir el DataFrame a una lista de diccionarios
    data = df.to_dict(orient='records')
    
    return data

