"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.ADT import minpq as mpq
from DISClib.ADT import indexminpq as impq
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import graph as gr
from DISClib.Algorithms.Graphs import scc
from DISClib.Algorithms.Graphs import dijsktra as djk
from DISClib.Algorithms.Graphs import bellmanford as bf
from DISClib.Algorithms.Graphs import bfs
from DISClib.Algorithms.Graphs import dfs
from DISClib.Algorithms.Graphs import prim
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf
import math

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    #TODO: Inicializar las estructuras de datos
    analyzer={
            'vuelos':mp.newMap(numelements=430
                                    ,
                                                maptype='PROBING'),
            'aeropuertos_mapa':mp.newMap(numelements=430
                                    ,
                                                maptype='PROBING'),
            'aviacion_carga_distancia': gr.newGraph(datastructure='ADJ_LIST',
                                              directed=True,
                                              size=430,
                                             ),
                                    
            'aviacion_carga_tiempo': gr.newGraph(datastructure='ADJ_LIST',
                                              directed=True,
                                              size=430,
                                              ),
            'aviacion_comercial_distancia': gr.newGraph(datastructure='ADJ_LIST',
                                              directed=True,
                                              size=430,
                                              ),
            'aviacion_comercial_tiempo':  gr.newGraph(datastructure='ADJ_LIST',
                                              directed=True,
                                              size=430,
                                              ),
            'militar_distancia':  gr.newGraph(datastructure='ADJ_LIST',
                                              directed=True,
                                              size=430,
                                              ),            'aviacion_comercial_tiempo':  gr.newGraph(datastructure='ADJ_LIST',
                                              directed=True,
                                              size=430,
                                              ),
            'militar_tiempo':  gr.newGraph(datastructure='ADJ_LIST',
                                              directed=True,
                                              size=430,
                                              ),            'aviacion_comercial_tiempo':  gr.newGraph(datastructure='ADJ_LIST',
                                              directed=True,
                                              size=430,
                                              ),
        
    }
    return analyzer

def add_aeropuerto(analyzer, aeropuerto):
    #función que crea un mapa con los aeropuertos
    aeropuertos_mapa= analyzer['aeropuertos_mapa']
    id_aeropuerto= aeropuerto['ICAO']
    mp.put(aeropuertos_mapa, id_aeropuerto, aeropuerto)
    
def carga_grafos_mapa_vuelos(analyzer, vuelos):
    #función que carga todos los grafos y el mapa de vuelos
    grafo_carga_d= analyzer['aviacion_carga_distancia']
    grafo_comercial_d= analyzer['aviacion_comercial_distancia']
    grafo_militar_d= analyzer['militar_distancia']
    grafo_carga_t=analyzer['aviacion_carga_tiempo'] 
    grafo_comercial_t= analyzer['aviacion_comercial_tiempo']
    grafo_militar_t= analyzer['militar_tiempo']
    add_vertices(analyzer, vuelos, grafo_carga_d, 'distancia')
    add_vertices(analyzer, vuelos, grafo_comercial_d, 'distancia')
    add_vertices(analyzer, vuelos, grafo_militar_d, 'distancia')
    add_vertices(analyzer, vuelos, grafo_carga_t, 'tiempo')
    add_vertices(analyzer, vuelos, grafo_comercial_t, 'tiempo')
    add_vertices(analyzer, vuelos, grafo_militar_t, 'tiempo')
    add_vuelo(analyzer, vuelos)
    

def add_vertices(analyzer, vuelos, grafo, tipo):
    #función que adiciona vertices
    grafo_carga=grafo
    origen= vuelos['ORIGEN']
    contiene_o= gr.containsVertex(grafo_carga, origen)
    destino= vuelos['DESTINO']
    contiene_d= gr. containsVertex(grafo_carga, destino)
    arco= gr.getEdge(grafo_carga, origen,destino)
    mapa_aeropuertos= analyzer['aeropuertos_mapa']
    t=0
    if contiene_o:
        if contiene_d:
            if arco != None:
                t+=1
            else:
                gr.addEdge(grafo_carga, origen, destino, calc_arco(mapa_aeropuertos, vuelos, origen, destino, tipo))
                
        else:
            gr.insertVertex(grafo_carga, destino)
            gr.addEdge(grafo_carga, origen, destino, calc_arco(mapa_aeropuertos, vuelos, origen, destino, tipo))
            
    else:
        gr.insertVertex(grafo_carga, origen)
        if contiene_d:
            gr.addEdge(grafo_carga, origen, destino, calc_arco(mapa_aeropuertos, vuelos, origen, destino, tipo))
        else:
            gr.insertVertex(grafo_carga, destino)
            gr.addEdge(grafo_carga, origen, destino, calc_arco(mapa_aeropuertos, vuelos, origen, destino, tipo))
            
def calc_arco(mapa_aeropuertos, vuelos, origen, destino, tipo):
    #función que adiciona arcos, si es un grafo de distancia utiliza la fórmula Harvesine y si es de tiempol, solo extrae el tiempo del vuelo
    if tipo=='distancia':
        R=6372.8
        pareja_origen= mp.get(mapa_aeropuertos, origen)
        datos_origen=me.getValue(pareja_origen)
        pareja_destino= mp.get(mapa_aeropuertos, destino)
        datos_destino=me.getValue(pareja_destino)
        lat_o= math.radians(float((datos_origen['LATITUD']).replace(',', '.')))
        lon_o= math.radians(float((datos_origen['LONGITUD']).replace(',', '.')))
        lat_d=  math.radians(float((datos_destino['LATITUD']).replace(',', '.')))
        lon_d=  math.radians(float((datos_destino['LONGITUD']).replace(',', '.')))
        dlat = lat_o - lat_d
        dlon = lon_o - lon_d
        a = math.sin(dlat / 2)**2 + math.cos(lat_o) * math.cos(lat_d) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = R * c
        return distance
    elif tipo=='tiempo':
        tiempo= vuelos['TIEMPO_VUELO']
        return tiempo
         
def add_vuelo(analyzer, vuelos):
    #función que crea el mapa de vuelos
    mapa_vuelos= analyzer['vuelos']
    nombre_vuelo= formato_id(vuelos)
    mp.put(mapa_vuelos, nombre_vuelo, vuelos)
    
def formato_id(vuelos):
    #función que formatea los ids del mapa de vuelos 
    nombre= vuelos['ORIGEN']
    nombre= nombre +'/' + vuelos['DESTINO']
    return nombre

def reporte_de_Carga(analyzer):
    aeropuertos_cargados= analyzer['aeropuertos_mapa']
    total_aeropuertos_cargados= lt.size(mp.keySet(aeropuertos_cargados))
    vuelos_cargados= analyzer['vuelos']
    total_vuelos_cargados= lt.size(mp.keySet(vuelos_cargados))
    arbol_comercial= analyzer['aviacion_comercial_distancia']
    arbol_carga= analyzer['aviacion_carga_distancia']
    arbol_militar= analyzer['militar_distancia']
    listas_comercial=listas(arbol_comercial, aeropuertos_cargados)
    listas_carga=listas(arbol_carga, aeropuertos_cargados)
    listas_militar=listas(arbol_militar, aeropuertos_cargados)
    return total_aeropuertos_cargados, total_vuelos_cargados, listas_comercial, listas_carga, listas_militar

def listas(arbol, aeropuertos_cargados):
    lista_vertices= gr.vertices(arbol)
    lista_orden= lt.newList('ARRAY_LIST')
    for i in lt.iterator(lista_vertices):
        elementos= i + '/' + str(gr.degree(arbol, i))
        lt.addLast(lista_orden, elementos)
    merg.sort(lista_orden, degrees_cmp)
    lista_primeros= lt.subList(lista_orden, 1, 5)
    lista_ultimos= lt.subList(lista_orden, lt.size(lista_orden)-5, 5)
    lt_primeros= lt.newList('ARRAY_LIST')
    lt_ultimos= lt.newList('ARRAY_LIST')
    for i in lt.iterator(lista_primeros):
        command= i.split('/')
        key= command[0]
        pareja=  mp.get(aeropuertos_cargados, key)
        valor=me.getValue(pareja)
        valor['Concurrencia comercial']= command[1]
        lt.addLast(lt_primeros, valor)
    for i in lt.iterator(lista_ultimos):
        command= i.split('/')
        key= command[0]
        pareja=  mp.get(aeropuertos_cargados, key)
        valor=me.getValue(pareja)
        valor['Concurrencia comercial']= command[1]
        lt.addLast(lt_ultimos, valor)
    return [lt_primeros, lt_ultimos]

def degrees_cmp(dato1, dato2):
    ver1 = dato1.split('/')
    vertice1 = int(ver1[1])
    vertice_name1 = ver1[0]
    ver2 = dato2.split('/')
    vertice2 = int(ver2[1])
    vertice_name2 = ver2[0]

    if vertice1 == vertice2:
        return vertice_name1 < vertice_name2  
    else:
        return vertice1 < vertice2 



# Funciones para agregar informacion al modelo

def add_data(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    pass


# Funciones para creacion de datos

def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    pass


# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    pass


def req_1(data_structs):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    pass


def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    pass


def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    pass


def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pass


def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    pass

# Funciones de ordenamiento


def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    pass


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass
