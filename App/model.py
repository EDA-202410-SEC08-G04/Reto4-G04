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
    tipo_vuelo= vuelos['TIPO_VUELO']
    if tipo_vuelo=='AVIACION_CARGA':
       add_vertices(analyzer, vuelos, grafo_carga_t, 'tiempo')
       add_vertices(analyzer, vuelos, grafo_carga_d, 'distancia')
       
    elif tipo_vuelo=='AVIACION_COMERCIAL':
       add_vertices(analyzer, vuelos, grafo_comercial_d, 'distancia')
       add_vertices(analyzer, vuelos, grafo_comercial_t, 'tiempo')
       
    elif tipo_vuelo=='MILITAR':
      add_vertices(analyzer, vuelos, grafo_militar_d, 'distancia')
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
        tiempo= float(vuelos['TIEMPO_VUELO'])
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
    #Función que recolecta toda la informacion que se requiere para la impresion de la carga
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
    #Función que organiza por primeros 5 y últimos 5 
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
    #Función de comparación
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


def req_1(data_structs):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    pass


def haversine(lat1, lon1, lat2, lon2):
    R=6372.8
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distancia = R* c
    return distancia

def compare_harvesine_distance(dic1, dic2):
    key1 = next(iter(dic1))
    key2 = next(iter(dic2))
    if key1 < key2:
        return True
    else:
        return False
    
def req_2(data_structs, input_lat_origen, input_long_origen, input_lat_destino, input_long_destino):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    grafo_comercial_dis = data_structs['aviacion_comercial_distancia']
    grafo_comercial_tiempo = data_structs['aviacion_comercial_tiempo']
    vertices_comerciales = gr.vertices(grafo_comercial_dis)
    mapa_aeropuertos = data_structs['aeropuertos_mapa']
    input_lat_origen = float(input_lat_origen.replace(',', '.'))
    input_long_origen = float(input_long_origen.replace(',', '.'))
    input_lat_destino = float(input_lat_destino.replace(',', '.'))
    input_long_destino = float(input_long_destino.replace(',', '.'))
    lista_dis_origen = lt.newList('ARRAY_LIST')
    lista_dis_destino = lt.newList('ARRAY_LIST')
    
    #Encontrar los aeropuertos origen y destino más cercanos a los ingresados
    for vertice in lt.iterator(vertices_comerciales):
        valor_id_aeropuerto = me.getValue(mp.get(mapa_aeropuertos, vertice))
        latitud = valor_id_aeropuerto['LATITUD']
        latitud = float(latitud.replace(',', '.'))
        longitud = valor_id_aeropuerto['LONGITUD']
        longitud = float(longitud.replace(',', '.'))
        calculo_harvesine_origen = haversine(latitud, longitud, input_lat_origen, input_long_origen)
        calculo_harvesine_destino = haversine(latitud, longitud, input_lat_destino, input_long_destino)
        diccionario_o = {calculo_harvesine_origen: valor_id_aeropuerto}
        diccionario_d = {calculo_harvesine_destino: valor_id_aeropuerto}
        lt.addLast(lista_dis_origen, diccionario_o)
        lt.addLast(lista_dis_destino, diccionario_d)  
    merg.sort(lista_dis_origen, compare_harvesine_distance)
    merg.sort(lista_dis_destino, compare_harvesine_distance)
    aeropuerto_inicial = lt.firstElement(lista_dis_origen)
    aeropuerto_final = lt.firstElement(lista_dis_destino)
    llave_aer_inicial = next(iter(aeropuerto_inicial))
    llave_aer_final = next(iter(aeropuerto_final))
    valor_aer_inicial = aeropuerto_inicial[llave_aer_inicial]
    valor_aer_final = aeropuerto_final[llave_aer_final]

    if float(llave_aer_inicial) > 30 or float(llave_aer_final) > 30:
        nombre_aer_inicial = valor_aer_inicial['NOMBRE']
        nombre_aer_final = valor_aer_final['NOMBRE']
        print ("No  se  ejecutó la  búsqueda ya que la distancia entre lo ingresado y los aeropuertos, supera los 30km. Sin embargo, el aeropuerto origen más cercano es: ", nombre_aer_inicial, " con una distancia de: ", llave_aer_inicial, " desde el punto ingresado. Y el aeropuerto destino más cercano es: ", nombre_aer_final, " con una distancia de: ", llave_aer_final, " desde el punto ingresado.")
    
    # Algoritmo Dijkstra
    search = djk.Dijkstra(grafo_comercial_dis, valor_aer_inicial['ICAO'])
    path = djk.pathTo(search, valor_aer_final['ICAO'])
    distancia_total = (djk.distTo(search, valor_aer_final['ICAO']) + llave_aer_inicial + llave_aer_final)
    cant_aero_visitados = (lt.size(path)+1)
    
    # ordena la cola
    ordenado = lt.newList('ARRAY_LIST')
    for item in lt.iterator(path):
        lt.addFirst(ordenado, item)
        
    # acceder a la información de los aeropuertos
    codigos = lt.newList("ARRAY_LIST")   
    for id in lt.iterator(ordenado):
        if id == lt.firstElement(ordenado):
            lt.addLast(codigos, id['vertexA'])
        lt.addLast(codigos, id['vertexB'])
        
    lista_final = lt.newList("ARRAY_LIST")
    for line in lt.iterator(codigos):
        info_aeropuerto = me.getValue(mp.get(mapa_aeropuertos, line))
        lt.addLast(lista_final, info_aeropuerto)

    #sacar tiempo total del recorrido
    search= djk.Dijkstra(grafo_comercial_tiempo, valor_aer_inicial['ICAO'])
    tiempo_total = djk.distTo(search, valor_aer_final['ICAO'])
    return distancia_total, cant_aero_visitados, lista_final, tiempo_total

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

def comparacion_arbol(aero1, aero2):
    #ordena de mayor a menor
    concurrencia1, icao1 = aero1
    concurrencia2, icao2 = aero2
    if concurrencia1 > concurrencia2:
        return 1
    elif concurrencia1 < concurrencia2:
        return -1
    else:
        if icao1 < icao2:
            return 1
        elif icao1 > icao2:
            return -1
        else:
            return 0

def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    mapa_aeropuertos = data_structs['aeropuertos_mapa']
    grafo_militar_dis = data_structs['militar_distancia']
    grafo_militar_tiempo = data_structs['militar_tiempo']
    
    # aeropuerto con mayor importancia militar (concurrencia)
    vertices_militares = gr.vertices(grafo_militar_dis)
    arbol_militar = om.newMap(cmpfunction=comparacion_arbol)
    for aeropuerto in lt.iterator(vertices_militares):
        num_salen = int(gr.outdegree(grafo_militar_dis, aeropuerto))
        num_llegan = int(gr.indegree(grafo_militar_dis, aeropuerto))
        grado_total = num_salen + num_llegan
        info = me.getValue(mp.get(mapa_aeropuertos, aeropuerto))
        info["concurrencia"] = grado_total
        om.put(arbol_militar, (grado_total, aeropuerto), info)
    aeropuerto_mayor = om.maxKey(arbol_militar)
    print ("AEROPUERTO MAYOR", aeropuerto_mayor)
    
    


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
