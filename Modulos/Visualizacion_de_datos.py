from Funciones_json import*


def mostrar_ciudades(ciudades, criterio, valor):
    encontrados = []
    
    for codigo, detalles in ciudades.items():
        if detalles.get(criterio) == valor:
            encontrados.append({**{'CIUDAD': codigo}, **detalles})
    
    if encontrados:
    
        print(f"{'CIUDAD':<10} {'CODIGO POSTAL':<15} {'POBLACION':<10} {'PAIS':<10} ")
        print("-" * 90)
        for item in encontrados:
            print(f"{item['CIUDAD']:<10} {item['codigo postal']:<15} {item['poblacion']:<10} {item['pais']:<10}")
        print("-" * 90)
    else:
        print("No se encontraron resultados para la búsqueda.")


def mostrar_ciudad():
    try:
            data = cargar_datos("ciudades.json", "d")

            nombre_ciudad = input('Ingrese el nombre de la ciudad que desea ver: \n ')
            if data.get(nombre_ciudad,None) != None:
                print(f"{'CIUDAD':<10} {'CODIGO POSTAL':<15} {'POBLACION':<10} {'PAIS':<10} ")
                print("-" * 90)
                print(f'{nombre_ciudad:<10},{data[nombre_ciudad]["codigo postal"]:<15},{data[nombre_ciudad]["poblacion"]:<10},{data[nombre_ciudad]["pais"]:<10}')
            else:
                print("Resultado no apto para busqueda...")
    except Exception as e:
            print(f"Ocurrió un error: {e}")

            
