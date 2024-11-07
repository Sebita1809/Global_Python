from funciones import *
from Clases import *
lista_ADN = {}
##aaaaaa,gggggg,cccccc,tttttt,gggggg,cccccc
##actggg,aggggg,aggggg,aggggg,gggggg,gggggg
##actggg,aggggg,gggggg,gggggg,gggggg,gggggg
##actggg,cggggg,aggggg,aggggg,cggggg,cggggg
##actggg,ctgggg,atgggg,acgggg,ccgggg,ctgggg
while True:
    
    inicializar_menu()
    respuesta = int(input("Ingrese la opcion: "))
    if respuesta == 1:
        nombreADN = input("Ingrese un nombre para el ADN que desea registrar:\n").upper()
        while True:
            mostrar_matriz_ejemplo()
            ADN = input("Ahora ingrese el ADN de la siguiente forma: fila 1,fila 2,fila 3,... ¡RECUERDE QUE DEBE INGRESAR TODAS LAS FILAS SEPERADAS POR UNA ',' :\n").upper()
            ADN_lista = ADN.split(",")
            verificador = verificar_adn(ADN_lista)
            if verificador == None or verificador == []:
                pass
            else:
                lista_ADN[nombreADN] = ADN_lista
                print(f"El ADN: {nombreADN} ingresado es {lista_ADN[nombreADN]}]")
                break
    elif respuesta == 2:
        nombreADN = input("Ingrese un nombre para el ADN que desea escanear:\n").upper()
        detector = Detector(nombreADN, ADN_lista)
        mutante_H = Detector.mutante_horizontal(ADN_lista)
        mutante_V = Detector.mutante_vertical(ADN_lista)
        mutante_D = Detector.mutante_diagonal1(ADN_lista)
        ##print(mutante_H)
        ##print(mutante_V)
        print(mutante_D)
