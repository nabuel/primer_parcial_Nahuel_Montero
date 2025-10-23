from Validaciones import *


def crear_matriz(filas: int,
                 columnas: int,
                 valor = False)->list:
    '''
    Crea una matriz de las dimensiones indicadas.

    Retorno: la matriz creada.
    '''

    matriz= []
    for _ in range(filas):
        fila_creada = [valor] * columnas
        matriz += [fila_creada]
    
    return matriz

def cargar_matriz_secuencial(matriz: list)-> list:
    '''
    Carga de manera secuencial la matriz con números enteros positivos.

    Retorno: la matriz creada.
    '''
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f"Está en la casilla {i}{j}")
            numero = input("Ingrese un número entero positivo: ")

            if validar_numero_positivo(numero) == False:
                print("Número no válido.")
                print(" ")
            
            while validar_numero_positivo(numero) == False:
                numero = input("Ingrese un número entero positivo: ")

                if validar_numero_positivo(numero) == False:
                    print("Número no válido.")
                    print(" ")
            
            matriz[i][j] += int(numero)

    return matriz

def calcular_total_array(array: list)-> int:
    '''
    Calcula la sumatoria de los números dentro del array.

    Retorno: el resultado de la sumatoria.
    '''
    total = 0
    for i in range(len(array)):
        total += array[i]
    
    return total

def buscar_numero(lista: list,
                  orden = False):
    '''
    Busca la posición del número menor de la lista. Si orden = True entonces buscar el número mayor.

    Retorno: La posición del número.
    '''
    numero = lista[0]
    indice = 0
    if orden:
        #Busca número mayor.
        for i in range(len(lista)):
            if numero < lista[i]:
                numero = lista[i]
                indice = i
    else:
        #Busca número menor.
        for i in range(len(lista)):
            if numero > lista[i]:
                numero = lista[i]
                indice = i


    return indice

def calcular_recaudacion(lista: list,
                         precios: list)-> int|float:
    '''
    Calcula la recaudación de la lista dada.

    Retorno: La totalidad de la recaudación.
    '''
    recaudacion = 0
    for i in range(len(lista)):
        recaudacion += lista[i] * precios[i]
    
    return recaudacion

def calcular_total_matriz(matriz: list)-> int:
    '''
    Calcula la sumatoria de la cantidad de elementos dentro de la matriz.

    Retorno: El resultado de la sumatoria.
    '''
    total = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            total += matriz[i][j]
    
    return total

def calcular_total_columna(matriz: list,
                           columna: int)-> int:
    '''
    Calcula la sumatoria de la cantidad de elementos dentro de la columna indicada.

    Retorno: El resultado de la sumatoria.
    '''
    total = 0
    for i in range(len(matriz)):
        total += matriz[i][columna] 

    return total

def calcular_porcentaje(total: int|float,
                        cantidad: int|float)-> int|float:
    '''
    Calcula el porcentaje de la cantidad indica en el total.

    Retorno: El resultado de la ecuación.
    '''
    porcentaje = (cantidad * 100) / total

    return porcentaje

def crear_array(longitud: int,
                valor = False)-> list:
    '''
    Crea una lista de la longitud indicada.

    Retorno: la lista creada.
    '''
    lista = [valor] * longitud

    return lista

def ordenar_array(array: list,
                  orden = False)-> list:
    '''
    Ordena la lista en el sentido indicado. 
    False ordena de menor a mayor.
    True ordena de mayor a menor. 

    Retorno: La lista ordenada.
    '''

    if orden:
        for i in range(len(array)):
            for j in range(len(array) - 1- i):
                numero = array[j]
                if numero < array[j + 1]:
                    array[j] = array[j + 1]
                    array[j + 1] = numero
    else:
        for i in range(len(array)):
            for j in range(len(array) - 1- i):
                numero = array[j]
                if numero > array[j + 1]:
                    array[j] = array[j + 1]
                    array[j + 1] = numero
    
    return array


