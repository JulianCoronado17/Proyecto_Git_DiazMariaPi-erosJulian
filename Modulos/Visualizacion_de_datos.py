from main import*
from Funciones_json import*

RUTA_JSON="ciudades.json"

def verdatos(RUTA_JSON):
    datos_json=cargar_datos(RUTA_JSON, "d")
    print(datos_json)
