from funciones import *
from Clases import *

##TGTTTT,GTGGCG,CCGTAA,AGGGCA,CGGCCC,CGAACC
##TACAAC,GAGTCG,CACAGC,TTCGCA,GCCCGA,TTCTAT
ADN = []
while True:
    inicializar_menu()
    while True:
        try:
            respuesta = int(input("Ingrese la opcion: "))
            break
        except ValueError:
            print("El caracter ingresado no es valido")
            inicializar_menu()
    if respuesta == 1:
        while True:
            mostrar_matriz_ejemplo()
            ADN = input("Ahora ingrese el ADN de la siguiente forma: fila 1,fila 2,fila 3,... ¡RECUERDE QUE DEBE INGRESAR TODAS LAS FILAS SEPERADAS POR UNA ',' :\n").upper()
            ADN = ADN.split(",")
            print(ADN)
            verificador = verificar_adn(ADN)
            if verificador != None:
                print("El ADN se ingresó correctamente")
                break
    elif respuesta == 2:
        print(ADN)
        Detector(ADN)
        ##print("Se detectaron mutantes en el ADN ingresado") if detector.detectar_mutantes(ADN) == True else print("No se detectaron mutantes en el ADN ingresado")
    elif respuesta == 3:
        Mutador(ADN).registrar_respuesta()
    elif respuesta == 4:
        Sanador(ADN)
    elif respuesta == 5:
        mostrar_en_formato_ADN(ADN)
    elif respuesta == 6:
        print("Gracias por usar nuestro programa")
        print("Saliendo....")
        break
    else: print("La opcion ingresada no corresponde con alguna opcion del menú")