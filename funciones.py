def inicializar_menu():
    print("Ingrese el numero de la operacion que desea realizar")
    print("""
            1 - Ingresar ADN
            2 - Detectar mutante
            3 - Mutar ADN
            4 - Sanar ADN
            5 - Salir
        """)

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
            print("Será redirigido nuevamente al menú") if verificador > 0 else print("Su ADN se ha registrado correctamente")
            return[] if verificador > 0 else ADN