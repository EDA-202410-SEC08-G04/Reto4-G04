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
 """

import config as cf
import model
import time
import csv
import tracemalloc

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller():
    """
    Crea una instancia del modelo
    """
    #TODO: Llamar la función del modelo que crea las estructuras de datos
    analyzer=model.new_data_structs()
    return analyzer


# Funciones para la carga de datos

def load_aeropuertos(analyzer, aeropuertos):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    file_aeropuertos=cf.data_dir + 'data/' + aeropuertos
    input_file_2 = csv.DictReader(open(file_aeropuertos, encoding="utf-8"),
                                delimiter=";")
    for aeropuerto in input_file_2:
        model.add_aeropuerto(analyzer, aeropuerto)


def load_vuelos(analyzer, vuelos):
    file_vuelos=cf.data_dir + 'data/' + vuelos
    input_file_1 = csv.DictReader(open(file_vuelos, encoding="utf-8"),
                                delimiter=";")
    for vuelo in input_file_1:
         model.carga_grafos_mapa_vuelos(analyzer, vuelo)

    
def load(analyzer, aeropuertos, vuelos):
    aeropuertos= load_aeropuertos(analyzer, aeropuertos)
    vuelos= load_vuelos(analyzer, vuelos)
    tiempo_inicial = time.time()
    model.calcular_concurrencia_por_categoria(analyzer)
    total_aeropuertos_cargados, total_vuelos_cargados, listas_comercial, listas_carga, listas_militar= model.reporte_de_Carga(analyzer)
    tiempo_final = time.time()
    tiempo_total = (tiempo_final - tiempo_inicial)*1000
    return total_aeropuertos_cargados, total_vuelos_cargados, listas_comercial, listas_carga, listas_militar, tiempo_total

# Funciones de ordenamiento

def sort(control):
    """
    Ordena los datos del modelo
    """
    #TODO: Llamar la función del modelo para ordenar los datos
    pass


# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Llamar la función del modelo para obtener un dato
    pass


def req_1(analyzer, lat1, lon1, lat2, lon2):
    """
    Retorna el resultado del requerimiento 1
    """
    tiempo_inicial = time.time()
    lista_camino_encontrado, distancia_total, tiempo_total, num_aeropuertos_visitados, punto_cercano_o, punto_cercano_d= model.req_1(analyzer, lat1, lon1, lat2, lon2)
    tiempo_final = time.time()
    tiempo_p = (tiempo_final - tiempo_inicial)*1000
    return lista_camino_encontrado, distancia_total, tiempo_total, num_aeropuertos_visitados, punto_cercano_o, punto_cercano_d, tiempo_p

def req_2(control, input_lat_origen, input_long_origen, input_lat_destino, input_long_destino):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    tiempo_inicial = time.time()
    distancia_total, cant_aero_visitados, lista_final, tiempo_recorrido = model.req_2(control, input_lat_origen, input_long_origen, input_lat_destino, input_long_destino)
    tiempo_final = time.time()
    tiempo_total = (tiempo_final - tiempo_inicial)*1000
    return distancia_total, cant_aero_visitados, lista_final, tiempo_recorrido, tiempo_total

def req_3(control):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    tiempo_inicial = time.time()
    
        
    lista_rta, suma_distancias, num_posibles_trayectos, distancia=model.req_3(control)
    
    tiempo_final = time.time()
    tiempo_total = (tiempo_final - tiempo_inicial)*1000
    
        
    return lista_rta, suma_distancias, num_posibles_trayectos, distancia, tiempo_total



def req_4(control):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(control):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    tiempo_inicial = time.time()
    info_aer_mayor, dis_total_trayectos, lista_final, num_trayectos =model.req_5(control)
    tiempo_final = time.time()
    tiempo_total = (tiempo_final - tiempo_inicial)*1000
    return info_aer_mayor, dis_total_trayectos, lista_final, num_trayectos, tiempo_total

def req_6(control,M_aeropuertos):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    tiempo_inicial = time.time()
    info_aer_mayor = model.req_6(control,M_aeropuertos)
    tiempo_final = time.time()
    tiempo_total = (tiempo_final - tiempo_inicial)*1000
    return info_aer_mayor, tiempo_total


def req_7(control):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass


def req_8(control):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed

def get_memory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def delta_memory(stop_memory, start_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory
