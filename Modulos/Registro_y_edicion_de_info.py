import json
from Funciones_json import*




def registro_ciudades():
    while True:
        try:
            data = cargar_datos("ciudades.json", "d")

            nombre_ciudad = input('Ingrese el nombre de la ciudad que desea registrar: \n ')

            if nombre_ciudad == '':
                print('saliendo...')
                break
            else:
                if data.get(nombre_ciudad, None) is None:
                    ciudad={}
                    ciudad['codigo postal']=input('Ingrese el codigo postal de la ciudad: \n')
                    ciudad['poblacion']=input('Ingrese la poblacion de la ciudad: \n')
                    ciudad['pais']=input('Ingrese el nombre del pais de la ciudad')
                    print(ciudad)
                    validacion = int(input(f'Esta seguro que desea guardar la siguiente informacion \n {ciudad} \n1.SI \n2.NO \n:'))
                    while True:
                        if validacion == 1:
                            data[nombre_ciudad] = ciudad
                            guardar_datos(data, 'ciudades.json')
                            break
                        elif validacion == 2:
                            print("Usted selecciono 2.NO, por favor reinicie el proceso")
                            break
                        else:
                            print('Número no válido')
                else:
                    print('Ciudad ya registrada...')
        except Exception as e:
            print(f"Ocurrió un error: {e}")





registro_ciudades()












