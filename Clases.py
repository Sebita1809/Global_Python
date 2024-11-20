import random
from funciones import *
class Detector:
    def __init__(self, ADN:list):
        try:
            self.ADN = ADN
            self.ADN_invertido = invertir_matriz(self.ADN)
            self.mutantes_encontrados = 0
            self.detectar_mutantes(self.ADN)
            print(self.detectar_mutantes(self.ADN))
        except Exception:
            print(f"Recuerde que debe ingresar un ADN primero")

    def detectar_mutantes(self, ADN:list):
        self.mutante_horizontal(ADN)
        self.mutante_vertical(ADN)
        self.mutante_diagonal1(ADN)
        self.mutante_diagonal2(ADN)
        self.mutante_diagonal_inversas(ADN)
        return True if self.mutantes_encontrados > 0 else False

    def mutante_horizontal(self, ADN:list):
        return True if self.verificador(ADN) == 1 else False
    
    def mutante_vertical(self, ADN:list):
        columna = []
        columnas = []
        for x in range(0, len(ADN)):
            for i in range(0 , len(ADN)):
                columna.append(ADN[i][x])
                if len(columna)%6 == 0:
                    palabra = ''.join(columna)
                    columnas.append(palabra)
                    columna = []
        self.mutantes_encontrados += self.verificador(columnas)
        return True if self.verificador(columnas) == 1 else False

    def mutante_diagonal1(self, ADN:list):
        diagonales = []    
        for cl in range(len(ADN)):
            diagonal = []
            for fila in range(len(ADN)):
                columna = cl + fila
                if columna < len(ADN):
                    diagonal.append(ADN[columna][fila])
                    if len(diagonal) >= (6 - cl) and cl <= 2:
                        palabra = ''.join(diagonal)
                        diagonales.append(palabra)
                        diagonal = []
        self.mutantes_encontrados += self.verificador(diagonales)
        return True if self.verificador(diagonales) == 1 else False
    
    def mutante_diagonal2(self, ADN:list):
        diagonales = []
        for fi in range(len(ADN)):
            diagonal = []
            for cl in range(len(ADN)):
                fila = fi + cl
                if fila < len(ADN):
                    diagonal.append(ADN[cl][fila])
                if len(diagonal) >= (6 - fi) and fi <= 2:
                    palabra = ''.join(diagonal)
                    diagonales.append(palabra)
                    diagonal = []                
        self.mutantes_encontrados += self.verificador(diagonales)
        return True if self.verificador(diagonales) == 1 else False
    
    def mutante_diagonal_inversas(self, ADN:list):
        self.mutante_diagonal1(invertir_matriz(ADN))
        self.mutante_diagonal2(invertir_matriz(ADN))

            # atatat,agagag,acacac,atatat,agagag,acacac

            # tatttt,ggaggg,cccacc,ttttat,ggggga,cccccc

            # ttattt,gggagg,ccccac,ttttta,ggggga,ccccca

            # tttttt,aggggg,cacccc,ttattt,gggagg,ccccac     

            # tttttt,gggggg,accccc,tatttt,ggaggg,cccacc

            # ttttta,ggggag,cccacc,ttattt,gagggg,accccc

    def verificador(self, ADN):
        encontrar_mutante = 0
        for i in range(0, 6):
            encontrar_mutante = 0
            palabra = ADN[i]
            for j in range(0,len(palabra)-1):
                encontrar_mutante +=1 if palabra[j] == palabra[j+1] else 0
            if encontrar_mutante >=3:
                break
        return 1 if encontrar_mutante >= 3 else 0

class Mutador:
    def __init__(self, ADN):
        self.ADN = ADN
        self.base_nitrogenada = random.choice(["A","C","G","T"])

    def crear_mutante(self):
        pass

    def registrar_respuesta(self):
        mostrar_menu_mutador()
        respuesta = int(input("Ingrese su respuesta:\n"))
        if respuesta == 1:
            Radiacion(self.ADN)
        elif respuesta == 2:
            Virus(self.ADN)
        elif respuesta == 3:
            print("Saliendo...")

class Radiacion(Mutador):
    def __init__(self, ADN):
            super().__init__(ADN)
            self.posicion_horizontal = 0
            self.posicion_vertical = 0
            self.tipo_radiacion = "" 
            self.base_nitrogenada = self.base_nitrogenada
            self.indicar_tipo_radiacion()
            self.indicar_posiciones()
            self.crear_mutante(self.base_nitrogenada, self.tipo_radiacion, self.posicion_vertical) if self.tipo_radiacion == "H" else self.crear_mutante(self.base_nitrogenada, self.tipo_radiacion, self.posicion_horizontal)

    def indicar_tipo_radiacion(self):
        while True:
            self.tipo_radiacion = input("Ingrese el tipo de radiacion ('V' vertical) o ('H' horizontal):\n").upper()
            if self.tipo_radiacion == "H" or self.tipo_radiacion == "V":
                break
            else:
                print("Se ingreso una opcion invalida")

    def indicar_posiciones(self):
        while True:
            self.posicion_horizontal = int(input("Ingrese la posicion horizontal donde desea que comience el mutante:\n"))
            self.posicion_vertical = int(input("Ingrese la posicion vertical donde desea que comience el mutante:\n"))
            if self.tipo_radiacion == "H":
                if self.posicion_vertical > 2: 
                    print("Debido a que el largo de los mutante es de 4, no es compatible la posicion vertical ingresada")
                else: 
                    break
            else:
                if self.posicion_horizontal > 2: print("Debido a que el largo de los mutante es de 4, no es compatible la posicion horizontal ingresada")
                else: break

    def crear_mutante(self, base_nitrogenada:str, orientacion:str, posicion_inicial:int):
        posicion = posicion_inicial
        if orientacion == "H":
            print(self.radiacion_horizontal(base_nitrogenada,posicion))
        else:
            print(self.radiacion_vertical(base_nitrogenada, posicion))

    def radiacion_horizontal(self, celula_nitrogenada:str, posicion_inicial:int):
        tope = 0 
        palabra = list(self.ADN[self.posicion_horizontal])
        for i in range(posicion_inicial, len(palabra)):
            palabra[i] = celula_nitrogenada
            tope += 1
            if tope == 4: break
        palabra = ''.join(palabra)
        self.ADN[self.posicion_horizontal] = palabra
        return self.ADN

    def radiacion_vertical(self, celula_nitrogenada:str, posicion_inicial:int):
        tope = 0 
        for i in range(posicion_inicial, len(self.ADN)):
            palabra = list(self.ADN[i])
            palabra[self.posicion_vertical] = celula_nitrogenada
            tope += 1
            palabra = ''.join(palabra)
            self.ADN[i] = palabra
            if tope == 4: break
        return self.ADN

class Virus(Mutador):
    def __init__(self, ADN):
        try:
            super().__init__(ADN)
            self.posicion_horizontal = 0
            self.posicion_vertical = 0
            self.tipo_virus = ""
            self.base_nitrogenada = self.base_nitrogenada
            self.definir_tipo_virus()
            self.definir_posicion()
            self.crear_mutante(self.base_nitrogenada, self.posicion_vertical)
        except Exception:
            print("Recuerde que debe ingresar un ADN primer")

    def definir_tipo_virus(self):
        mostrar_menu_virus()
        respuesta = int(input("Ingrese su respuesta:\n"))
        if respuesta == 1 or respuesta == 2:
            self.tipo_virus = "Normal" if respuesta == 1 else "Invertido"
        else:
            print("La opcion ingresada no es valida")
            self.definir_tipo_virus()
    
    def definir_posicion(self):
        print("Desde que posicion vertical desea empezar el virus?")
        self.posicion_vertical = int(input("Ingrese la posicion:\n"))
        print("Desde que posicion horizontal desea empezar el virus?")
        self.posicion_horizontal = int(input("Ingrese la posicion:\n"))
        if self.posicion_horizontal > 2 or self.posicion_vertical > 2:
            if self.tipo_virus == "Normal":
                print("Debido a que los virus tienen una longitud de 4, las posiciones no pueden excederse de 2")
                self.definir_posicion()
        elif self.posicion_horizontal < 0 or self.posicion_vertical < 0:
            print("Ha ingresado una posicion que no existe")
            self.definir_posicion()
        else: 
            if self.tipo_virus == "Invertido":
                print("Debido a que los virus tienen una longirud de 4, las posiciones no pueden ser menor de 3")
                self.definir_posicion()

    def crear_mutante(self, base_nitrogenada:str, posicion_inicial:int):
            print(self.virus_diagonal(posicion_inicial, base_nitrogenada)) if self.tipo_virus == "Normal" else print(self.virus_diagonal_invertida(posicion_inicial, base_nitrogenada))

    def virus_diagonal(self, posicion_vertical:int, base_nitrogenada:str):
        tope = 0
        aumento = 1
        for i in range(self.posicion_horizontal, len(self.ADN)-1):
            palabra = list(self.ADN[i])
            if i == self.posicion_horizontal:
                palabra[posicion_vertical] = base_nitrogenada  
            else: 
                palabra[posicion_vertical+aumento] = base_nitrogenada
                aumento += 1
                tope += 1
                palabra = ''.join(palabra)
                self.ADN[i] = palabra
                if tope == 4: break
        return self.ADN

    def virus_diagonal_invertida(self, posicion_vertical:int, base_nitrogenada:str):
        tope = 0
        aumento = 1
        for i in range(self.posicion_horizontal, len(self.ADN)-1):
            palabra = list(self.ADN[i])
            if i == self.posicion_horizontal:
                palabra[posicion_vertical] = base_nitrogenada 
            else:
                palabra[posicion_vertical-aumento] = base_nitrogenada
                aumento += 1
            tope += 1
            palabra = ''.join(palabra)
            self.ADN[i] = palabra
            if tope == 4: break
        return self.ADN

class Sanador:
    def __init__(self, ADN:list):
        try:
            self.bases_nitrogenadas = ["A","C","G","T"]
            self.ADN = ADN
            self.ADN_invertido = invertir_matriz(self.ADN)
            self.detectar_mutantes(self.ADN)
            self.sanar_mutantes(self.ADN)
            self.mostrar_ADN_sano()
        except Exception:
            pass

    def detectar_mutantes(self, ADN:list):
        detector = Detector(ADN)
        return True if detector.detectar_mutantes(ADN) == True else False
    
    def sanar_mutantes(self,ADN:list):
        if self.detectar_mutantes(ADN) == True:
            while self.detectar_mutantes(ADN) == True:
                for i in range(0, 6):
                    palabra = list(ADN[i])
                    for j in range(len(palabra)):
                        palabra[j] = random.choice(self.bases_nitrogenadas)
                    palabra = ''.join(palabra)
                    ADN[i] = palabra
                self.ADN_invertido = invertir_matriz(ADN)
                self.ADN = ADN
                self.detectar_mutantes(ADN)
        return self.ADN

    def mostrar_ADN_sano(self):
        print(f"El ADN sanado se muestra a continuacion: {self.sanar_mutantes(self.ADN)}")