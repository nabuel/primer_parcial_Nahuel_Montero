def obtener_digito(mensaje: str)-> int:
    '''
    Obtiene un número entero de un digito.

    Retorno: el número obtenido.
    '''
    numero = input(mensaje)
    if len(numero)> 1:
        print("Ingrese un número de un dígito.")
        numero = input(mensaje)
    while type(numero) != int:
        #Si no es numero
        if ord(numero) > 57 or ord(numero) < 48:
            print("Ingrese un número de un dígito.")
            numero = input(mensaje)
        elif len(numero)> 1:
            print("Ingrese un número de un dígito.")
            numero = input(mensaje)
        else:
            numero = int(numero)
    
    return numero

def validar_numero_positivo(numero: str)-> bool:
    '''
    Valida si el número ingresado es positivo y entero.
    
    Retorno: True en caso de que lo sea.
             False en caso contrario.
    '''
    
    for i in range(len(numero)):
        if ord(numero[i]) > 57 or ord(numero[i]) < 48:
            return False
    
    return True
