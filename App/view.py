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
    total_aeropuertos_cargados, total_vuelos_cargados, listas_comercial, listas_carga, listas_militar, tiempo = controller.load(control, vuelos, aeropuertos)
    print ("El tiempo que se demora algoritmo en encontrar la solució es: ", tiempo, " milisegundos")
    print('El total de aeropuertos cargados es:', total_aeropuertos_cargados)
    print('El total de vuelos cargados es:', total_vuelos_cargados)

    def prepare_headers():
        return {
            'Nombre del aeropuerto:': [],
            'Identificador ICAO del aeropuerto:': [],
            'Ciudad del aeropuerto:': [],
            'Concurrencia:': []
        }

    def fill_headers(headers, data_list, concurrencia_key):
        for i in lt.iterator(data_list):
            headers['Nombre del aeropuerto:'].append(i['NOMBRE'])
            headers['Identificador ICAO del aeropuerto:'].append(i['ICAO'])
            headers['Ciudad del aeropuerto:'].append(i['CIUDAD'])
            headers['Concurrencia:'].append(i[concurrencia_key])

    headers_carga_p5 = prepare_headers()
    headers_carga_u5 = prepare_headers()
    fill_headers(headers_carga_p5, listas_carga[0], 'Concurrencia carga')
    fill_headers(headers_carga_u5, listas_carga[1], 'Concurrencia carga')

    headers_comercial_p5 = prepare_headers()
    headers_comercial_u5 = prepare_headers()
    fill_headers(headers_comercial_p5, listas_comercial[0], 'Concurrencia comercial')
    fill_headers(headers_comercial_u5, listas_comercial[1], 'Concurrencia comercial')

    headers_militar_p5 = prepare_headers()
    headers_militar_u5 = prepare_headers()
    fill_headers(headers_militar_p5, listas_militar[0], 'Concurrencia militar')
    fill_headers(headers_militar_u5, listas_militar[1], 'Concurrencia militar')

    print('Los primeros 5 aeropuertos de carga con mayor concurrencia son:')
    print(tabulate(headers_carga_p5, headers='keys', tablefmt='simple_grid'))
    
    print('Los últimos 5 aeropuertos de carga con mayor concurrencia son:')
    print(tabulate(headers_carga_u5, headers='keys', tablefmt='simple_grid'))
    
    print('Los primeros 5 aeropuertos comerciales con mayor concurrencia son:')
    print(tabulate(headers_comercial_p5, headers='keys', tablefmt='simple_grid'))
    
    print('Los últimos 5 aeropuertos comerciales con mayor concurrencia son:')
    print(tabulate(headers_comercial_u5, headers='keys', tablefmt='simple_grid'))
    
    print('Los primeros 5 aeropuertos militares con mayor concurrencia son:')
    print(tabulate(headers_militar_p5, headers='keys', tablefmt='simple_grid'))
    
    print('Los últimos 5 aeropuertos militares con mayor concurrencia son:')
    print(tabulate(headers_militar_u5, headers='keys', tablefmt='simple_grid'))





       
    

def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control, lat1, lon1, lat2, lon2):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    lista_camino_encontrado, distancia_total, tiempo_total, num_aeropuertos_visitados, punto_cercano_o, punto_cercano_d, tiempo= controller.req_1(control, lat1, lon1, lat2, lon2)
    print ("El tiempo que se demora algoritmo en encontrar la solució es: ", tiempo, " milisegundos")
    if lista_camino_encontrado==None:
        print('No se enontraron aeropuertos en los rangos de búsqueda')
        print('Estas son las distancias encontradas entre los aeropuertos más cercanos del punto de origen y el punto de destino:')
        print('Codigo del aeropuerto mas cercano al punto de origen:')
        po=  punto_cercano_o.split('/')
        po_codigo= po[0]
        po_distancia= po[1]
        print(po_codigo)
        print('Distancia entre el aeropuerto mas cercano y el punto de origen:')
        print(po_distancia)
        print('Codigo del aeropuerto mas cercano al punto de destino:')
        pd=  punto_cercano_d.split('/')
        pd_codigo= pd[0]
        pd_distancia= pd[1]
        print(pd_codigo)
        print('Distancia entre el aeropuerto mas cercano y el punto de destino:')
        print(pd_distancia)
    else:
        print('La cantidad de vuelos cargados es:')
        print(num_aeropuertos_visitados)
        print('La distancia total del trayecto es:')
        print(distancia_total)
        print('El tiempo total del trayecto en minutos es:')
        print(tiempo_total)
        print('Esta es la secuencia del trayecto') 
        print('El primer elemento es el Aeropuerto de origen y el ultimo es el Aeropuerto de destino:')
        headers_camino = {
        'Nombre del aeropuerto:': [],
        'Identificador ICAO del aeropuerto:': [],
        'Ciudad del aeropuerto:': [],
        'Pais del aeropuerto:': []
        }
        for i in lt.iterator(lista_camino_encontrado):
            headers_camino['Nombre del aeropuerto:'].append(i['NOMBRE'])
            headers_camino['Identificador ICAO del aeropuerto:'].append(i['ICAO'])
            headers_camino['Ciudad del aeropuerto:'].append(i['CIUDAD'])
            headers_camino['Pais del aeropuerto:'].append(i['PAIS'])
            
        print(tabulate(headers_camino, headers='keys', tablefmt='simple_grid'))


def print_req_2(control, input_lat_origen, input_long_origen, input_lat_destino, input_long_destino):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    distancia_total, cant_aero_visitados, lista_final, tiempo_recorrido, tiempo_total = controller.req_2(control, input_lat_origen, input_long_origen, input_lat_destino, input_long_destino)
    print ("El tiempo que se demora algoritmo en encontrar la solució es: ", tiempo_total, " milisegundos")
    print ("La distancia total del camino entre el punto de origen y el de destino es: ", distancia_total)
    print ("El número de aeropuertos que se visitan en el camino encontrado: ", cant_aero_visitados)
    headers_req2 = {'Identificador ICAO del aeropuerto:': [],
        'Nombre del aeropuerto:': [],
        'Ciudad del aeropuerto:': [],
        'País del aeropuerto:': []
    }
    for i in lt.iterator(lista_final):
        headers_req2['Identificador ICAO del aeropuerto:'].append(i['ICAO'])
        headers_req2['Nombre del aeropuerto:'].append(i['NOMBRE'])
        headers_req2['Ciudad del aeropuerto:'].append(i['CIUDAD'])
        headers_req2['País del aeropuerto:'].append(i['PAIS'])
    print(tabulate(headers_req2, headers='keys', tablefmt='simple_grid'))
    print ("Tiempo del trayecto total: ", tiempo_recorrido, " minutos")
    

def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    rta, suma_distancias, num_posibles_trayectos, distancia,tiempo_total=controller.req_3(control)
    print ("El tiempo que se demora algoritmo en encontrar la solució es: ", tiempo_total, " milisegundos")
    print ("La distancia total de todos los cmanios posibles es ", suma_distancias)
    print ("El número de trayectos posibles: ", num_posibles_trayectos)
    print ("La distancia total del camino entre el punto de origen y el de destino es: ", distancia)
    
    headers_req3 = {'Identificador ICAO del aeropuerto': [],
        'Nombre del aeropuerto': [],
        'Ciudad del aeropuerto': [],
        'País del aeropuerto': []
        
    }
    for aeropuerto in lt.iterator(rta):
        
            headers_req3['Identificador ICAO del aeropuerto'].append(aeropuerto['ICAO'])
            headers_req3['Nombre del aeropuerto'].append(aeropuerto['NOMBRE'])
            headers_req3['Ciudad del aeropuerto'].append(aeropuerto['CIUDAD'])
            headers_req3['País del aeropuerto'].append(aeropuerto['PAIS'])
                
            
    print(tabulate(headers_req3, headers='keys', tablefmt='simple_grid'))
    


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
    info_aer_mayor, dis_total_trayectos, lista_final, num_trayectos, tiempo_total=controller.req_5(control)
    print ("El tiempo que se demora algoritmo en encontrar la solució es: ", tiempo_total, " milisegundos")
    headers_aero_mayor = {'ICAO del aeropuerto de mayor importancia militar:': [],
        'Nombre del aeropuerto:': [],
        'Ciudad del aeropuerto:': [],
        'País del aeropuerto:': [], 
        'Concurrencia del aeropuerto:': []}
    headers_aero_mayor['ICAO del aeropuerto de mayor importancia militar:'].append(info_aer_mayor['ICAO'])
    headers_aero_mayor['Nombre del aeropuerto:'].append(info_aer_mayor['NOMBRE'])
    headers_aero_mayor['Ciudad del aeropuerto:'].append(info_aer_mayor['CIUDAD'])
    headers_aero_mayor['País del aeropuerto:'].append(info_aer_mayor['PAIS'])
    headers_aero_mayor['Concurrencia del aeropuerto:'].append(info_aer_mayor['concurrencia'])
    print ("La información del aeropuerto más importante según la concurrencia milita: ")
    print(tabulate(headers_aero_mayor, headers='keys', tablefmt='simple_grid'))
    print("La distancia total de los trayectos sumados es: ", dis_total_trayectos)
    print ("El número  total  de  trayectos  posibles  partiendo  desde  el  aeropuerto  de mayor importancia es: ", num_trayectos)
    headers_trayectos = {
        'ICAO origen:': [],
        'Aeropuerto origen:': [],
        'Ciudad origen:': [],
        'País origen:': [], 
        'ICAO destino:': [], 
        'Aeropuerto destino:': [],
        'Ciudad destino:': [], 
        'Pais destino:': [], 
        'Distancia trayecto:': [],
        'Tiempo trayecto:': []}
    for i in lt.iterator(lista_final):
        headers_trayectos['ICAO origen:'].append(i['ICAO origen']),
        headers_trayectos['Aeropuerto origen:'].append(i['aeropuerto origen']),
        headers_trayectos['Ciudad origen:'].append(i['ciudad origen']),
        headers_trayectos['País origen:'].append(i['pais origen']),
        headers_trayectos['ICAO destino:'].append(i['ICAO destino']),
        headers_trayectos['Aeropuerto destino:'].append(i['aeropuerto destino']),
        headers_trayectos['Ciudad destino:'].append(i['ciudad destino']),
        headers_trayectos['Pais destino:'].append(i['pais destino']),
        headers_trayectos['Distancia trayecto:'].append(i['distancia trayecto']),
        headers_trayectos['Tiempo trayecto:'].append(i['tiempo trayecto'])
    print ("La información de la secuencia de trayectos encontrados: ")
    print(tabulate(headers_trayectos, headers='keys', tablefmt='simple_grid'))
    
    
def print_req_6(control, M_aeropuertos):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    
    info_aer_mayor, lista_rta, tiempo_total = controller.req_6(control,M_aeropuertos)
    print ("El tiempo que se demora algoritmo en encontrar la solució es: ", tiempo_total, " milisegundos")
    headers_aero_mayor = {'ICAO del aeropuerto de mayor importancia comercial:': [],
        'Nombre del aeropuerto:': [],
        'Ciudad del aeropuerto:': [],
        'País del aeropuerto:': [], 
        'Concurrencia del aeropuerto:': []}
    headers_aero_mayor['ICAO del aeropuerto de mayor importancia comercial:'].append(info_aer_mayor['ICAO'])
    headers_aero_mayor['Nombre del aeropuerto:'].append(info_aer_mayor['NOMBRE'])
    headers_aero_mayor['Ciudad del aeropuerto:'].append(info_aer_mayor['CIUDAD'])
    headers_aero_mayor['País del aeropuerto:'].append(info_aer_mayor['PAIS'])
    headers_aero_mayor['Concurrencia del aeropuerto:'].append(info_aer_mayor['concurrencia'])
    print ("La información del aeropuerto más importante según la concurrencia comercial: ")
    print(tabulate(headers_aero_mayor, headers='keys', tablefmt='simple_grid'))
    
    
    
    headers_vuelos = {'ICAO:': [],
            'Nombre del aeropuerto:': [],
            'Ciudad del aeropuerto:': [],
            'País del aeropuerto:': []}
    
    for rta in lt.iterator(lista_rta):
        headers_vuelos['ICAO:'].append(rta['ICAO'])
        headers_vuelos['Nombre del aeropuerto:'].append(rta['NOMBRE'])
        headers_vuelos['Ciudad del aeropuerto:'].append(rta['CIUDAD'])
        headers_vuelos['País del aeropuerto:'].append(rta['PAIS'])
    

    print(tabulate(headers_vuelos, headers='keys', tablefmt='simple_grid'))
        
    


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
            lat1=input('Ingrese la latitud del punto de origen que quiere consultar:')
            lon1=input('Ingrese la longitud del punto de origen que quiere consultar:')
            lat2=input('Ingrese la latitud del punto de destino que quiere consultar:')
            lon2=input('Ingrese la longitud del punto de destino que quiere consultar:')
            print_req_1(control, lat1, lon1, lat2, lon2)
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
            M_aeropuertos=input("aero?: ")
            print_req_6(control,M_aeropuertos)

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
