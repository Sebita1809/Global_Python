
while True:
    print("Ingrese el numero de la operacion que desea realizar")
    print("""
            1 - Ingresar ADN
            2 - Detectar mutante
            3 - Mutar ADN
            4 - Sanar ADN
            5 - Salir
        """)
    respuesta = int(input("Ingrese la opcion: "))
    if respuesta == 1:
        nombreADN = input("Ingrese un nombre para el ADN que desea registrar").upper()
        ADN = input("Ahora ingrese el ADN de la siguiente forma: AGATCA,GATICA,CAACAT,...").upper()
        ADN_lista = ADN.split(",")
        for palabra in ADN_lista:
            if len(palabra) < 6 or len(palabra) > 6:
                print("ha ingresado mal el ADN, debido a que no ingreso la cantidad correcta de datos")
                break;
            for letra in len(palabra):
                if letra != "A" or "C" or "T" or "G":
                    print("Los datos ingresados no corresponden a celulas nitrogenadas")
                    break;
        print(ADN_lista)