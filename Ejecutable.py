from funciones import *
from Clases import *

##TGTTTT,GTGGCG,CCGTAA,AGGGCA,CGGCCC,CGAACC
##TACAAG,GAGTGG,CACGGC,TTGGCA,GGCCGA,GTCTAT

ADN = []
## El programa se ejecutará siempre y cuando el usuario no selecccione la opcion salir (opcion 6)
while True:
    ## Le mostramos el menú al usuario para que ingrese que desea hacer
    inicializar_menu()
    ## Este bucle While sirve para evaluar si el usuario no ingresó datos de otro tipo que no sea int
    while True:
        try:
            respuesta = int(input("Ingrese la opcion: "))
            break
        except ValueError:
            print("El caracter ingresado no es valido")
            inicializar_menu()
    if respuesta == 1:
        ## Este bucle While sirve para que el usuario ingrese bien el ADN, si este no cumple con los parametros
        ## de VERIFICIAR_ADN, se le solicitará ingresarlo nuevamente hasta que esté bien
        while True:
            mostrar_matriz_ejemplo()
            ADN = input("Ahora ingrese el ADN de la siguiente forma: fila 1,fila 2,fila 3,... ¡RECUERDE QUE DEBE INGRESAR TODAS LAS FILAS SEPERADAS POR UNA ',' :\n").upper()
            ADN = ADN.split(",")
            verificador = verificar_adn(ADN)
            if verificador != None:
                print("El ADN se ingresó correctamente")
                break
    ## Si el usuario ingresa la opcion 2, se invocará a la clase Detector y sw imprimirá por pantalla el resultado del analisis
    elif respuesta == 2:
        detector = Detector(ADN).detectar_mutantes(ADN)
        print(f"Despues del analizis realizado, el resultado es '{detector}', así que si posee mutantes.") if detector == True else print(f"Despues del analizis realizado, el resultado es '{detector}', así que no posee mutantes.")
    ## Si el usuario ingresa la opcion 3, se invocará a la clase Mutador
    elif respuesta == 3:
        Mutador(ADN).registrar_respuesta()
    ## Si el usuario ingresa la opcion 4, se invocará a la clase Sanador
    elif respuesta == 4:
        Sanador(ADN)
    ## Si el usuario ingresa la opcion 5, se llamará a la funcion MOSTRAR_EN_FORMATO_ADN
    elif respuesta == 5:
        mostrar_en_formato_ADN(ADN)
    ## Si el usuario ingresa la opcion 6, se saldrá del programa
    elif respuesta == 6:
        print("Gracias por usar nuestro programa")
        print("Saliendo....")
        break
    ## Si el usuario ingresa un valor distinto al de las opciones, se indicará la equivocacion y volverá a 
    ## pedirle que ingrese una opcion
    else: print("La opcion ingresada no corresponde con alguna opcion del menú")