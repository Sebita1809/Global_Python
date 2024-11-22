## Esta funcion le muestra al usuario el menú
def inicializar_menu():
    print("Por favor ingrese una opcion")
    print("""
            1 - Ingresar ADN
            2 - Detectar mutante
            3 - Mutar ADN
            4 - Sanar ADN
            5 - Mostrar en formato ADN
            6 - Salir
        """)

## Esta funcion le muestra al usuario como es una ADN y como debe ingresarlo en el programa
def mostrar_matriz_ejemplo():
    print("Le recordamos que el formato general del ADN es asi:")
    print("""
            A A A A A A -> fila 1
            A A A A A A -> fila 2
            A A A A A A -> fila 3
            A A A A A A -> fila 4
            A A A A A A -> fila 5
            A A A A A A -> fila 6
        """)
    print("Recuerde que las celulas nitrogenadas que conforman el ADN son: 'A' 'C' 'T' 'G'")

## Esta funcion le permite al usuario ver tanto el ADN ingresado, como los mutados y el sanado, en formato
## original del ADN (es decir, en formato matriz)
def mostrar_en_formato_ADN(ADN):
    for i in range(len(ADN)):
        palabra = ' '.join(ADN[i])
        print(palabra)

## Esta funcion le muestra al ususario el menu de la clase Mutador
def mostrar_menu_mutador():
    print("""
        Seleccionar el tipo de mutante que desea crear:
        1)- Radiación
        2)- Virus
        3)- Salir
        """)

## Esta funcion le muestra al ususario el menu de la clase Virus
def mostrar_menu_virus():
    print("""
        Seleccione la direccion del virus:
        1)- Izquierda a derecha
        2)- Derecha a izquierda
        """)

## La funcion VERIFICAR_ADN se encarga de controlar que el ADN tenga el largo correcto (filas y columnas) y
## que las celulas ingresadas pertenezcan a las celulas nitrogenadas que conforman un ADN
def verificar_adn(ADN:list):
    celulas_nitrogenadas = "ACTG"
    if len(ADN) != 6:
        print("El ADN ingresado, no cuenta con el largo correcto")  
    else:
        for i in range(len(ADN)):
            if len(ADN[i]) != 6:
                print("Ha ingresado mal el ADN, debido a que no ingresó la cantidad correcta de datos")
                return None
            for letra in ADN[i]:
                if letra not in celulas_nitrogenadas:
                    print(f"Ha ingresado mal el ADN, debido a que la letra {letra} no corresponde una celula nitrogenada")
                    return None
        return ADN

## Esta funcion se encarga de invertir el ADN (invierte las fila)
## fila 1 (AGTC) --> fila 1 (CTGA)
def invertir_matriz(ADN:list):
    matriz_invertida = []
    for i in range(len(ADN)): 
        palabra = ADN[i]
        matriz_invertida.append(palabra[::-1])
    return matriz_invertida

## Esta funcion se encarga de verificar que las posiciones que ingrese en usuario sean acordes al tamaño del ADN
def verificar_posiciones(posicion1:int, posicion2:int):
    if posicion1 <= 0 or posicion1 > 6 or posicion1 == None:
        print("La posicion ingresada es incompatible con largo del ADN")
        return True
    elif posicion2 <= 0 or posicion2 > 6 or posicion2 == None:
        print("La posicion ingresada es incompatible con largo del ADN")
        return True
    else: return False