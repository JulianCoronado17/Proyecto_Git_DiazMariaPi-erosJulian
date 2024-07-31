import json


def cargar_datos(RUTA_JSON, Tipo):
    try:
        with open(RUTA_JSON, "r") as file:
            Diccionario = json.load(file)
        print("INFORMACION ACTUALIZADA!!")
        return Diccionario
    except FileNotFoundError:
        if Tipo == "d":
            return {}
        elif Tipo == "l":
            return []
        


def guardar_datos(datos_json,RUTA_JSON):
    try:
        contenido = json.dumps(datos_json, indent=4)
        with open(RUTA_JSON, "w") as file:
            file.write(contenido)
        print("Datos guardados exitosamente!!")
    except Exception:
        print("Error al guardar datos")