from Funciones import *

depositos = ["Haedo", "Tigre", "San Martín", "Florencio Varela", "Mercedes", "Ezeiza" ,"José León Suarez"]

materiales = ["cemento","ladrillos", "cal", "arena","varillas de acero","pintura."]

planilla = crear_matriz(7,6,0)

precios = [10000,20000,30000,40000,50000,60000]

bandera = True

while bandera:
    print("--------------")
    print("1- Obtener existencias.")
    print("2- Calcular por cada depósito la cantidad total de elementos almacenados entre todos los materiales.")
    print("3- Buscar el nombre del material que almacenó menos elementos en cada depósito.")
    print("4- Buscar el depósito que almacenó la máxima cantidad de elementos de cada material.")
    print("5- Depósito con mayor recaudación.")
    print("6- Cantidad de depósitos que hayan almacenado más de 50.000 elementos entre los 5 materiales.")
    print("7- Porcentaje de elementos de cada material sobre el total de elementos almacenados.")
    print("8- Generar un informe con la recaudación de cada depósito.")
    print("--------------")

    desicion = obtener_digito("Elija una de las opciones: ")

    match desicion:
        case 1:
            planilla = cargar_matriz_secuencial(planilla)
        case 2:
            total = 0
            for i in range(len(planilla)):
                total = calcular_total_array(planilla[i])
                print(f"En el deposito de {depositos[i]} hay {total} materiales.")
            
            print(" ")
            
        case 3:
            for i in range(len(planilla)):
                indice = buscar_numero(planilla[i])
                print(f"El material que menos se almacenó en {depositos[i]} es {materiales[indice]}")
            print(" ")
        case 4:

            for j in range(len(planilla[0])):
                cantidad_material = planilla[0][j]
                material_actual = materiales[j]
                deposito_mayor = depositos[0]
                for i in range(len(planilla)):
                    indice = buscar_numero(planilla[i], True)
                    if material_actual == materiales[indice] and cantidad_material < planilla[i][indice]:
                        cantidad_material = planilla[i][indice]
                        deposito_mayor = depositos[i]

                print(f"El depósito con mayor stock de {materiales[j]} es {deposito_mayor}")
                print(" ")
        case 5:
            deposito_mayor = depositos[0]
            recaudacion_mayor = calcular_recaudacion(planilla[0],precios)
            for i in range(len(planilla)):
                recaudacion = calcular_recaudacion(planilla[i], precios)
                if recaudacion_mayor < recaudacion:
                    recaudacion_mayor = recaudacion
                    deposito_mayor = depositos[i]
            
            print(f"El depósito con mayor recaudación es {deposito_mayor} y recaudó {recaudacion_mayor}$")
            print(" ")
        case 6:
            cantidad = 0
            for i in range(len(planilla)):
                if calcular_total_array(planilla[i]) > 50000:
                    cantidad += 1

            print(f"La cantidad de depósitos que almacenan más de 50000 materiales son {cantidad}.")
            print(" ")
        case 7:
            total_materiales = calcular_total_matriz(planilla)
            porcentaje_mayor = 0
            material_porcentaje_mayor = materiales[0]
            for j in range(len(planilla[0])):
                cantidad_material = calcular_total_columna(planilla, j)
                porcentaje = calcular_porcentaje(total_materiales, cantidad_material)
                print(f"El total de materiales en todos los depósitos es {total_materiales}, de los cuales el {porcentaje}% es de {materiales[j]}")
                if porcentaje_mayor < porcentaje:
                    porcentaje_mayor = porcentaje
                    material_porcentaje_mayor = materiales[j]
            
            print(f"El porcentaje mayor es de {material_porcentaje_mayor} con {porcentaje_mayor}%.")
            print(" ")
        case 8:
            lista_recaudacion = crear_array(len(depositos))
            for i in range(len(planilla)):
                lista_recaudacion[i] = calcular_recaudacion(planilla[i], precios)
            
            lista_recaudacion_ordenada = ordenar_array(lista_recaudacion, True)
            for j in range(len(lista_recaudacion_ordenada)):
                for n in range(len(lista_recaudacion)):
                    if lista_recaudacion_ordenada[i] == lista_recaudacion[j]:
                        print(f"La recaudación del depósito {depositos[n]} es: {lista_recaudacion_ordenada[j]}$")
                        
            print(" ")
        case _:
            salida = obtener_digito("Ingrese 1 si quiere salir del programa.")
            if salida == 1:
                bandera = False  