def inicializar_menu():
    print("Bienvenido a nuestro programa")
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

def verificar_adn(ADN):
    celulas_nitrogenadas = "ACTG"
    verificador = 0
    if len(ADN) != 6:
        print("El ADN ingresado, no cuenta con el largo correcto")  
    else:
        for i in range(len(ADN)):
            if len(ADN[i]) != 6:
                print("Ha ingresado mal el ADN, debido a que no ingreso la cantidad correcta de datos")
                verificador = 1
                break
            for letra in ADN[i]:
                if letra not in celulas_nitrogenadas:
                    print(f"La letra {letra} no corresponde una celula nitrogenada")
                    verificador = 1
                    break
        print("Por favor ingrese nuevamente el ADN") if verificador > 0 else print("Su ADN se ha registrado correctamente")
        return [] if verificador > 0 else ADN