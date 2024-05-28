"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert cf
from tabulate import tabulate
import traceback

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""





def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2-  Identificar si hay una ruta entre dos destinos turísticos")
    print("3- Identificar el itinerario con menos escalas entre dosdestinos turísticos")
    print("4- Determinar la red de trayectos comerciales decobertura máxima desde el aeropuerto con mayor concurrencia")
    print("5- Determinar la red de trayectos de carga de distanciamínima partiendo del aeropuerto con mayor concurrencia")
    print("6- Determinar la red de respuesta militar de menortiempo partiendo desde el aeropuerto con mayor importancia militar")
    print("7-  Obtener los caminos más cortos para la cobertura delos M aeropuertos más importantes del país ")
    print("8- Obtener el camino más corto en tiempo para llegarentre dos puntos turísticos")
    print("9- Graficar los resultados para cada uno de los requerimientos")
    print("0- Salir")
    



        
def load_data(control, vuelos, aeropuertos):
    """
    Carga los datos
    """
    total_aeropuertos_cargados, total_vuelos_cargados, listas_comercial, listas_carga, listas_militar = controller.load(control, vuelos, aeropuertos)
    print('El total de aeropeurtos cargados es:' + str(total_aeropuertos_cargados))
    print('El total de vvuelos cargados es:' + str(total_vuelos_cargados))
    headers_carga_p5 = {
        'Nombre del aeropuerto:': [],
        'Identificador ICAO del aeropuerto:': [],
        'Ciudad del aeropuerto:': [],
        'Concurrencia comercial:': []
    }
    headers_carga_u5 = {
        'Nombre del aeropuerto:': [],
        'Identificador ICAO del aeropuerto:': [],
        'Ciudad del aeropuerto:': [],
        'Concurrencia comercial:': []
    }

    headers_comercial_p5 = {
        'Nombre del aeropuerto:': [],
        'Identificador ICAO del aeropuerto:': [],
        'Ciudad del aeropuerto:': [],
        'Concurrencia comercial:': []
    }
    headers_comercial_u5 = {
        'Nombre del aeropuerto:': [],
        'Identificador ICAO del aeropuerto:': [],
        'Ciudad del aeropuerto:': [],
        'Concurrencia comercial:': []
    }
    headers_militar_p5 = {
        'Nombre del aeropuerto:': [],
        'Identificador ICAO del aeropuerto:': [],
        'Ciudad del aeropuerto:': [],
        'Concurrencia comercial:': []
    }
    headers_militar_u5 = {
        'Nombre del aeropuerto:': [],
        'Identificador ICAO del aeropuerto:': [],
        'Ciudad del aeropuerto:': [],
        'Concurrencia comercial:': []
    }
    p5_carga = listas_carga[0]
    u5_carga = listas_carga[1] 
    for i in lt.iterator(p5_carga):
        headers_carga_p5['Nombre del aeropuerto:'].append(i['NOMBRE'])
        headers_carga_p5['Identificador ICAO del aeropuerto:'].append(i['ICAO'])
        headers_carga_p5['Ciudad del aeropuerto:'].append(i['CIUDAD'])
        headers_carga_p5['Concurrencia comercial:'].append(i['Concurrencia comercial'])
    print('Los primeros 5 aeropuertos de carga con mayor concurrencia son:')
    print(tabulate(headers_carga_p5, headers='keys', tablefmt='simple_grid'))
    
    for i in lt.iterator(u5_carga):
        headers_carga_u5['Nombre del aeropuerto:'].append(i['NOMBRE'])
        headers_carga_u5['Identificador ICAO del aeropuerto:'].append(i['ICAO'])
        headers_carga_u5['Ciudad del aeropuerto:'].append(i['CIUDAD'])
        headers_carga_u5['Concurrencia comercial:'].append(i['Concurrencia comercial'])
    print('Los últimos 5 aeropuertos de carga con mayor concurrencia son:')   
    print(tabulate(headers_carga_u5, headers='keys', tablefmt='simple_grid'))  
    
    p5_comercial = listas_comercial[0]
    u5_comercial = listas_comercial[1]
    for i in lt.iterator(p5_comercial):
        headers_comercial_p5['Nombre del aeropuerto:'].append(i['NOMBRE'])
        headers_comercial_p5['Identificador ICAO del aeropuerto:'].append(i['ICAO'])
        headers_comercial_p5['Ciudad del aeropuerto:'].append(i['CIUDAD'])
        headers_comercial_p5['Concurrencia comercial:'].append(i['Concurrencia comercial'])
    print('Los primeros 5 aeropuertos comerciales con mayor concurrencia son:')   
    print(tabulate(headers_carga_p5, headers='keys', tablefmt='simple_grid'))
    
    for i in lt.iterator(u5_comercial):
        headers_comercial_u5['Nombre del aeropuerto:'].append(i['NOMBRE'])
        headers_comercial_u5['Identificador ICAO del aeropuerto:'].append(i['ICAO'])
        headers_comercial_u5['Ciudad del aeropuerto:'].append(i['CIUDAD'])
        headers_comercial_u5['Concurrencia comercial:'].append(i['Concurrencia comercial'])
    print('Los últimos 5 aeropuertos comerciales con mayor concurrencia son:')      
    print(tabulate(headers_carga_u5, headers='keys', tablefmt='simple_grid'))  

    p5_militar = listas_militar[0]
    u5_militar = listas_militar[1]

    for i in lt.iterator(p5_militar):
        headers_militar_p5['Nombre del aeropuerto:'].append(i['NOMBRE'])
        headers_militar_p5['Identificador ICAO del aeropuerto:'].append(i['ICAO'])
        headers_militar_p5['Ciudad del aeropuerto:'].append(i['CIUDAD'])
        headers_militar_p5['Concurrencia comercial:'].append(i['Concurrencia comercial'])
    print('Los primeros 5 aeropuertos militares con mayor concurrencia son:')       
    print(tabulate(headers_militar_p5, headers='keys', tablefmt='simple_grid'))
    
    for i in lt.iterator(u5_militar):
        headers_militar_u5['Nombre del aeropuerto:'].append(i['NOMBRE'])
        headers_militar_u5['Identificador ICAO del aeropuerto:'].append(i['ICAO'])
        headers_militar_u5['Ciudad del aeropuerto:'].append(i['CIUDAD'])
        headers_militar_u5['Concurrencia comercial:'].append(i['Concurrencia comercial'])
    print('Los últimos 5 aeropuertos militares con mayor concurrencia son:')      
    print(tabulate(headers_militar_u5, headers='keys', tablefmt='simple_grid')) 




def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    pass


def print_req_2(control, input_lat_origen, input_long_origen, input_lat_destino, input_long_destino):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    distancia_total, cant_aero_visitados, lista_final, tiempo_recorrido, tiempo_total = controller.req_2(control, input_lat_origen, input_long_origen, input_lat_destino, input_long_destino)
    print ("El tiempo que se demora algoritmo en encontrar la solució es: ", tiempo_total, " milisegundos")
    print ("La distancia total del camino entre el punto de origen y el de destino es: ", distancia_total)
    print ("El número de aeropuertos que se visitan en el camino encontrado: ", cant_aero_visitados)
    headers = {'Identificador ICAO del aeropuerto:': [],
        'Nombre del aeropuerto:': [],
        'Ciudad del aeropuerto:': [],
        'País del aeropuerto:': []
    }
    for i in lt.iterator(lista_final):
        headers['Identificador ICAO del aeropuerto:'].append(i['ICAO'])
        headers['Nombre del aeropuerto:'].append(i['NOMBRE'])
        headers['Ciudad del aeropuerto:'].append(i['CIUDAD'])
        headers['País del aeropuerto:'].append(i['PAIS'])
    print(tabulate(headers, headers='keys', tablefmt='simple_grid'))
    print ("Tiempo del trayecto total: ", tiempo_recorrido, " minutos")
    

def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    pass


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    controller.req_5(control)


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    pass


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


# Se crea el controlador asociado a la vista

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    control = controller.new_controller()
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            print("Cargando información de los archivos ....\n")
            aeropuertos= 'airports-2022.csv'
            vuelos='fligths-2022.csv'
            load_data(control, aeropuertos, vuelos)
            


        elif int(inputs) == 2:
            print_req_1(control)
            

        elif int(inputs) == 3:
            
            input_lat_origen = input("Ingrese la latitud del lugar origen: ")
            input_long_origen = input("Ingrese la longitud del lugar origen: ")
            input_lat_destino = input("Ingrese la latitud del lugar destino: ")
            input_long_destino = input("Ingrese la longitud del lugar destino: ")
            print_req_2(control, input_lat_origen, input_long_origen, input_lat_destino, input_long_destino)

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            print_req_7(control)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa")
            
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
