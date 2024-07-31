import json
from Modulos.Funciones_json import*




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





#registro_ciudades()


def modificacion_ciudades():
    while True:
        try:
            data = cargar_datos("ciudades.json", "d")

            nombre_ciudad = input('Ingrese el nombre de la ciudad que desea modificar: \n ')
            if data.get(nombre_ciudad,None) != None:
                criterios = ['codigo postal','poblacion','pais']
                n = 0
                for i in criterios:
                    n = n+1
                    print(n,i)
                eleccion = int(input('Digite el número de la opción que desea elegir: \n '))
                eleccion = eleccion-1
                elegido = criterios[eleccion]
                criterio = str(elegido)
                cambio= input(f'Ingrese los nuevos datos a cambiar para {nombre_ciudad }, en el campo de {criterio}: \n')
                validacion = int(input(f'Esta seguro que desea guardar la siguiente informacion \n {cambio} en el campo de {criterio} \n1.SI \n2.NO \n:'))
                while True:
                    if validacion == 1:
                        data[nombre_ciudad][criterio] = cambio
                        guardar_datos(data,"ciudades.json")
                        break
                    elif validacion == 2:
                        print("Usted selecciono 2.NO, por favor reinicie el proceso")
                        break
                    elif validacion != 1 or 2:
                        print('Numero no valido')

            else:
                print("Resultado no apto para modificacion de campo...")
        except Exception as e:
            print(f"Ocurrió un error: {e}")