def inicializar_menu():
    print("Por favor ingrese una opcion")
    print("""
            1 - Ingresar ADN
            2 - Detectar mutante
            3 - Mutar ADN
            4 - Sanar ADN
            5 - Salir
        """)

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

def invertir_matriz(ADN:list):
    arreglo = []
    matriz_invertida = []
    for i in range(len(ADN)):
        palabra = ADN[i]
        for j in range(len(ADN)-1, -1, -1):
            arreglo.append(palabra[j])
    for i in range(0,len(arreglo), 6):
        arreglo = arreglo[i:i + 6]
        palabra = ''.join(palabra)
        matriz_invertida.append(palabra)
    return matriz_invertida

def mostrar_menu_mutador():
    print("""
        Seleccionar el tipo de mutante que desea crear:
        1)- Radiación
        2)- Virus
        3)- Salir
        """)

def mostrar_menu_virus():
    print("""
        Seleccione la direccion del virus:
        1)- Izquierda a derecha
        2)- Derecha a izquierda
        """)

def verificar_posiciones(posicion1:int, posicion2:int):
    if posicion1 < 0 or posicion1 > 6:
        return True
    elif posicion2 < 0 or posicion2 > 6:
        return True
    else: return False