from Modulos.Visualizacion_de_datos import*
from Modulos.Registro_y_edicion_de_info import*

RUTA_JSON="ciudades.json"

mainmenu="""
1.Registro
2.Modificación
3.Visualización
4.Salir
"""

menu_verdatos="""
Escoja como desea Filtrar

1.Ver datos por Nombre
2.Ver datos por Codigo Postal
3.Ver datos por Pais
4.Rango de poblacion
"""

while True:
    print(mainmenu)
    opcmain=input("Escoja una opción: ")
    if opcmain =="1":
        registro_ciudades()
    elif opcmain == "2":
        pass
    elif opcmain == "3":
        while True:
            print("MOSTRAR CIUDADES")
            print("*"*70)
            print('1.Ver información por campo especifico')
            print('2.Ver información segun cantidad de poblacion')
            print('3.seleccion por nombre de ciudad')
    
            try:
                opc = int(input("Digite el número de la opción que desea elegir:  "))
                if opc == 1:
                    ciudades = cargar_datos("ciudades.json", "d")
                    criterios = ['codigo','codigo postal','pais']
                    n = 0
                    for i in criterios:
                        n = n+1
                        print(n,i)
                    eleccion = int(input('Digite el número de la opción que desea elegir: \n '))
                    eleccion = eleccion-1
                    elegido = criterios[eleccion]
                    criterio = str(elegido)
                    valor = input(f'Escriba la descripción que se encuentra en {criterios[eleccion]}:  ')
                    mostrar_ciudades(ciudades, criterio, valor)
                    continuar=int(input('¿Desea seguir buscando? \n1.Si \n2.No \n'))
                    if continuar == 1:
                        continue
                    elif continuar == 2:
                        print('saliendo...')
                        break
                elif opc != 1 or 2:
                    print('Opción no valida')
                elif opc == 2:
                    rango1=int(input("Ingrese un rango de población, desde"))
                    rango2=int(input("Ingrese un rango de población, hasta"))
                    for key, values in ciudades:
                        if ciudades['codigo postal'][values] >= rango1 and ciudades['codigo postal'][values] <= rango2:
                            for key, values in ciudades
                elif opc == 3:
                    mostrar_ciudad()
            
                elif opc != 1 or 2 or 3:
                    print('Opción no valida')
            except Exception as e:
                print(f"Ocurrió un error: {e}")
   
        
    elif opcmain == "4":
        print("Chao Potaxie")
        break
        

