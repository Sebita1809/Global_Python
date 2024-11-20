from funciones import *
from Clases import *
lista_ADN = {}
##
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
            print(ADN_lista)
            verificador = verificar_adn(ADN_lista)
            if verificador == None or verificador == []:
                pass
            else:
                lista_ADN[nombreADN] = ADN_lista
                print("El ADN se ingresó correctamente")
                break
    elif respuesta == 2:
        nombreADN = input("Ingrese un nombre para el ADN que desea escanear:\n").upper()
        matriz_invertida = Detector.invertir_matriz(ADN_lista)
        detector = Detector(ADN_lista, matriz_invertida)
        print(detector.detectar_mutantes())
    elif respuesta == 3:
        mutante = Mutador(ADN_lista).mostrar_menu()
    elif respuesta == 4:
        matriz_invertida = Detector.invertir_matriz(ADN_lista)
        Sanador(ADN_lista, matriz_invertida)
    elif respuesta == 5:
        nombreADN = input("Ingrese el nombre del ADN que desea ver\n")
        print(f"El ADN '{nombreADN}' es: {lista_ADN[nombreADN]}")
