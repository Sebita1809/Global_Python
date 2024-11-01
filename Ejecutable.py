from funciones import *

lista_ADN = {}
while True:
    inicializar_menu()
    respuesta = int(input("Ingrese la opcion: "))
    if respuesta == 1:
        nombreADN = input("Ingrese un nombre para el ADN que desea registrar:\n").upper()
        ADN = input("Ahora ingrese el ADN de la siguiente forma: AGATCA,GATICA,CAACAT,... :\n").upper()
        ADN_lista = ADN.split(",")
        lista_ADN[nombreADN] = verificar_adn(ADN_lista)
        print(lista_ADN)
