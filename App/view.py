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
    lista_camino_encontrado, distancia_total, tiempo_total, num_aeropuertos_visitados, punto_cercano_o, punto_cercano_d= controller.req_1(control, lat1, lon1, lat2, lon2)
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


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control, tipo):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    lista_recorrido,  distancia_total, num_trayectos, tiempo_total, nombre_aero_imp=controller.req_4(control, tipo)
    mapa_aeropuertos= controller.req4_mapa(control)
    if tipo== 'Si':
        print('El aeropuerto mas importante es ' + nombre_aero_imp + ' y es el primero en el trayecto')
        print('La distancia total de los trayectos es ' + str(distancia_total) )
        print('El tiempo total de los trayectos es ' + str(tiempo_total) )
        print('El numero total de trayectos posibles es ' + str(num_trayectos))
        print('Esta es la secuencia de trayectos encontrados:')
        for recorrido in lista_recorrido['elements']:
            origen = recorrido['Origen']
            destino = recorrido['Destino']
            distancia = recorrido['Distancia recorrida en el trayecto']
            tiempo = recorrido['El tiempo del trayecto es:']

            # Extraer y formatear la información del origen
            info_origen = origen[0].replace('El aeropuerto de origen es', '').split(', y su identificador es')
            nombre_origen = info_origen[0]
            icao_origen = info_origen[1]
            info_pais_ciudad_origen = origen[1].replace('Su pais y su ciuda son', '').split(' y ')
            pais_origen = info_pais_ciudad_origen[0]
            ciudad_origen = info_pais_ciudad_origen[1]

            # Extraer y formatear la información del destino
            info_destino = destino[0].replace('El aeropuerto de destino es', '').split(', y su identificador es')
            nombre_destino = info_destino[0]
            icao_destino = info_destino[1]
            info_pais_ciudad_destino = destino[1].replace('Su pais y su ciudad son', '').split(' y ')
            pais_destino = info_pais_ciudad_destino[0]
            ciudad_destino = info_pais_ciudad_destino[1]

            # Imprimir la información formateada
            print(f"Origen: {nombre_origen} ({icao_origen}) en {ciudad_origen}, {pais_origen}")
            print(f"Destino: {nombre_destino} ({icao_destino}) en {ciudad_destino}, {pais_destino}")
            print(f"Distancia recorrida en el trayecto: {distancia:.2f} km")
            print(f"El tiempo del trayecto es: {tiempo}")
            print("-" * 80)
        
    else:
        print('El aeropuerto mas importante es ' + nombre_aero_imp + ' y es el primero en el trayecto')
        print('La distancia total de los trayectos es ' + str(distancia_total) )
        print('El tiempo total de los trayectos es ' + str(tiempo_total) )
        print('El numero total de trayectos posibles es ' + str(num_trayectos))
        print('Esta es la secuencia de trayectos encontrados:')
    for recorrido in lista_recorrido['elements']:
        # Inicializar las variables para los nombres de los vértices
        vertexA = vertexB = None

        # Verificar si los nombres de los vértices son 'Origen' y 'Destino' o 'vertexA' y 'vertexB'
        if 'Origen' in recorrido and 'Destino' in recorrido:
            vertexA = recorrido['Origen']
            vertexB = recorrido['Destino']
        elif 'vertexA' in recorrido and 'vertexB' in recorrido:
            vertexA = recorrido['vertexA']
            vertexB = recorrido['vertexB']


        weight = recorrido['weight']

        # Obtener información de los aeropuertos
        aeropuertoA = mapa_aeropuertos.get(vertexA, {})
        aeropuertoB = mapa_aeropuertos.get(vertexB, {})

        nombreA = aeropuertoA.get('NOMBRE', 'Desconocido')
        ciudadA = aeropuertoA.get('CIUDAD', 'Desconocido')
        paisA = aeropuertoA.get('PAIS', 'Desconocido')

        nombreB = aeropuertoB.get('NOMBRE', 'Desconocido')
        ciudadB = aeropuertoB.get('CIUDAD', 'Desconocido')
        paisB = aeropuertoB.get('PAIS', 'Desconocido')

        # Imprimir la información formateada
        print(f"Origen: {nombreA} ({vertexA}) en {ciudadA}, {paisA}")
        print(f"Destino: {nombreB} ({vertexB}) en {ciudadB}, {paisB}")
        print(f"Distancia recorrida en el trayecto: {weight:.2f} km")
        print("-" * 80)
    pass


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass


def print_req_7(control, lat1, lon1, lat2, lon2):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    lista_camino_encontrado, distancia_total, tiempo_total, num_aeropuertos_visitados, punto_cercano_o, punto_cercano_d= controller.req_7(control, lat1, lon1, lat2, lon2)
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
            print_req_2(control)

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            tipo=input('Le gustaria ver la informacion de cada secuencia dentro de trayecto?(Si/No) ')
            print_req_4(control, tipo)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            lat1=input('Ingrese la latitud del punto de origen que quiere consultar:')
            lon1=input('Ingrese la longitud del punto de origen que quiere consultar:')
            lat2=input('Ingrese la latitud del punto de destino que quiere consultar:')
            lon2=input('Ingrese la longitud del punto de destino que quiere consultar:')
            print_req_7(control, lat1, lon1, lat2, lon2)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa")
            
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
