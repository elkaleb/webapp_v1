from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

    def file_loader_1_change(self, file, **event_args):
        if file is not None:
            # Llamar al servidor para procesar el archivo
            data = anvil.server.call('procesar_archivo', file)
            
            # Establecer los datos en el Repeating Panel
            self.repeating_panel_1.items = data
            alert("Archivo procesado con éxito y datos mostrados")


