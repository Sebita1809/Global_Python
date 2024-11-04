from funciones import *
from Clases import *


lista_ADN = {}
while True:
    inicializar_menu()
    respuesta = int(input("Ingrese la opcion: "))
    if respuesta == 1:
        nombreADN = input("Ingrese un nombre para el ADN que desea registrar:\n").upper()
        ADN = input("Ahora ingrese el ADN de la siguiente forma: AGATCA,GATCCA,CAACAT,... :\n").upper()
        ADN_lista = ADN.split(",")
        verificador = verificar_adn(ADN_lista)
        if verificador == None:
            pass
        else:
            lista_ADN[nombreADN] = ADN_lista
        print(lista_ADN)
    if respuesta == 2:
        nombreADN = input("Ingrese un nombre para el ADN que desea escanear:\n").upper()
        detector = Detector(nombreADN, ADN_lista)
        mutante_H = Detector.mutante_horizontal(ADN_lista)
        ##mutante_V = Detector.mutante_vertical(ADN_lista)
        print(mutante_H)
