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
    
def cmp_req1(dato1, dato2):
    #Función de comparación
    ver1 = dato1.split('/')
    vertice1 = float(ver1[1])
    vertice_name1 = ver1[0]
    ver2 = dato2.split('/')
    vertice2 = float(ver2[1])
    vertice_name2 = ver2[0]

    if vertice1 == vertice2:
        return vertice_name1 < vertice_name2  
    else:
        return vertice1 < vertice2 

    
def req_1(analyzer, lat1, lon1, lat2, lon2):
    grafo_distancia= analyzer['aviacion_comerciasl_distancia']
    grafo_tiempo= analyzer['aviacion_comercial_tiempo']
    mapa_aeropuertos= analyzer['aeropuertos_mapa']
    lista_vertices= gr.vertices(grafo_distancia)
    list_origen_posible= lt.newList('ARRAY_LIST')
    restantes_origen= lt.newList('ARRAY_LIST')
    list_destino_posible= lt.newList('ARRAY_LIST')
    restantes_destino= lt.newList('ARRAY_LIST')
    for i in lt.iterator(lista_vertices):
        pareja= mp.get(mapa_aeropuertos, i)
        valori=me.getValue(pareja)
        latio= math.radians(float((valori['LATITUD']).replace(',', '.')))
        lonio=math.radians(float((valori['LONGITUD']).replace(',', '.')))
        lat1r=math.radians(float((lat1.replace(',', '.'))))
        lon1r=math.radians(float((lon1.replace(',', '.'))))
        lat2r=math.radians(float((lat2.replace(',', '.'))))
        lon2r=math.radians(float((lon2.replace(',', '.'))))        
        dlato= latio-lat1r
        dlono= lonio-lon1r
        dlatd=latio-lat2r
        dlond=lonio-lon2r
        a = math.sin(dlato / 2)**2 + math.cos(latio) * math.cos(lat1r) * math.sin(dlono / 2)**2
        b = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        c= math.sin(dlatd / 2)**2 + math.cos(latio) * math.cos(lat2r) * math.sin(dlond / 2)**2
        d = 2 * math.atan2(math.sqrt(c), math.sqrt(1 - c))
        distance_origen = 6372.8 * b
        distance_destino= 6372.8 * d
        
        if distance_origen<= 30 and distance_destino<= 30:
            lt.addLast(list_origen_posible, i + '/' + str(distance_origen))
            lt.addLast(list_destino_posible, i + '/' + str(distance_destino))
        elif distance_origen>30 and distance_destino<=30:
            lt.addLast(list_destino_posible, i + '/' + str(distance_destino))
            lt.addLast(restantes_origen, i + '/' + str(distance_origen))
        elif distance_origen<=30 and distance_destino>30:
            lt.addLast(list_origen_posible, i + '/' + str(distance_origen))
            lt.addLast(restantes_destino, i + '/' + str(distance_destino))
        else:
            lt.addLast(restantes_origen, i + '/' + str(distance_origen))
            lt.addLast(restantes_destino, i + '/' + str(distance_destino))
    
    if lt.isEmpty(list_origen_posible)!= True and lt.isEmpty(list_destino_posible)!= True:
        merg.sort(list_origen_posible, cmp_req1)
        info_origen= lt.firstElement(list_origen_posible)
        split_origen= info_origen.split('/')
        punto_origen= split_origen[0]
        distancia_origen_aeropuerto= float(split_origen[1])
        merg.sort(list_destino_posible, cmp_req1)
        info_destino= lt.firstElement(list_destino_posible)
        split_destino= info_destino.split('/')
        punto_destino=split_destino[0]
        distancia_aeropuerto_destino= float(split_destino[1])
        search = dfs.DepthFirstSearch(grafo_distancia, punto_origen)
        if dfs.hasPathTo(search, punto_destino):
            camino= dfs.pathTo(search, punto_destino)
            lista_recorrido= lt.newList('ARRAY_LIST')
            while not st.isEmpty(camino): 
                vertice= st.pop(camino)
                lt.addLast(lista_recorrido, vertice)
            pares=lt.newList('ARRAY_LIST')
            for i in range(1, lt.size(lista_recorrido)): 
                par = lt.subList(lista_recorrido, i, 2) 
                if lt.size(par) == 2:
                    lt.addLast(pares, par)
            pares_consecutivos = lt.newList('ARRAY_LIST')
            for i in range(lt.size(lista_recorrido) - 1):
                vertice1 = lt.getElement(lista_recorrido, i + 1)
                vertice2 = lt.getElement(lista_recorrido, i + 2)
                lt.addLast(pares_consecutivos, [vertice1, vertice2])
            distancia_total=0
            tiempo_total= 0
            for e in lt.iterator(pares_consecutivos):
                vertice1= e[0]
                vertice2= e[1]
                arcod=gr.getEdge(grafo_distancia, vertice1, vertice2)
                distancia_total+= float(arcod['weight'])
                arcot=gr.getEdge(grafo_tiempo, vertice1, vertice2)
                tiempo_total+= int(arcot['weight'])
            distancia_total+= distancia_origen_aeropuerto
            distancia_total+= distancia_aeropuerto_destino
            num_aeropuertos_visitados= lt.size(lista_recorrido)
            lista_camino_encontrado= lt.newList('ARRAY_LIST')
            info_punto_o=mp.get(mapa_aeropuertos, punto_origen)
            valor_origen=me.getValue(info_punto_o)
            info_punto_d=mp.get(mapa_aeropuertos, punto_destino)
            valor_destino=me.getValue(info_punto_d)
            for n in lt.iterator(lista_recorrido):
                info_vertice=mp.get(mapa_aeropuertos, n)
                valor_vertice= me.getValue(info_vertice)
                lt.addLast(lista_camino_encontrado, valor_vertice)
            lt.addFirst(lista_camino_encontrado, valor_origen)
            lt.addLast(lista_camino_encontrado, valor_destino)
            punto_cercano_d=None
            punto_cercano_o=None
        else:
            lista_camino_encontrado=None
            distancia_total=None
            tiempo_total=None
            merg.sort(restantes_origen, cmp_req1)
            merg.sort(restantes_destino, cmp_req1)
            punto_cercano_o= lt.firstElement(restantes_origen)
            punto_cercano_d= lt.firstElement(restantes_destino)
    elif lt.isEmpty(list_origen_posible) or lt.isEmpty(list_destino_posible):
        lista_camino_encontrado=None
        distancia_total=None
        tiempo_total=None
        merg.sort(restantes_origen, cmp_req1)
        merg.sort(restantes_destino, cmp_req1)
        punto_cercano_o= lt.firstElement(restantes_origen)
        punto_cercano_d= lt.firstElement(restantes_destino)
    return lista_camino_encontrado, distancia_total, tiempo_total, num_aeropuertos_visitados, punto_cercano_o, punto_cercano_d




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
