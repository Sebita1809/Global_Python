import random
class Detector:
    def __init__(self, ADN, ADN_invertido):
        self.ADN = ADN
        self.ADN_invertido = ADN_invertido
        self.mutantes_encontrados = 0
        self.mutante = self.detectar_mutantes()
        self.mutante_horizontal()
        self.mutante_vertical()
        self.mutante_diagonal1()
        self.mutante_diagonal2()

    def crear_mutante(self):
        pass

    def detectar_mutantes(self):
        return True if self.mutantes_encontrados > 0 else False

    def mutante_horizontal(self):
        self.mutante += self.verificador(self.ADN)
        return True if self.verificador(self.ADN) == 1 else False
    
    def mutante_vertical(self):
        columna = []
        columnas = []
        for x in range(0, len(self.ADN)):
            for i in range(0 , len(self.ADN)):
                columna.append(self.ADN[i][x])
                if len(columna)%6 == 0:
                    palabra = ''.join(columna)
                    columnas.append(palabra)
                    columna = []
        self.mutantes_encontrados += self.verificador(columnas)
        return True if self.verificador(columnas) == 1 else False

    def mutante_diagonal1(self):
        diagonales = []    
        
        for cl in range(len(self.ADN)):
            diagonal = []
            for fila in range(len(self.ADN)):
                columna = cl + fila
                if columna < len(self.ADN):
                    diagonal.append(self.ADN[columna][fila])
                    if len(diagonal) >= (6 - cl) and cl <= 2:
                        palabra = ''.join(diagonal)
                        diagonales.append(palabra)
                        diagonal = []
        self.mutantes_encontrados += self.verificador(diagonales)
        return True if self.verificador(diagonales) == 1 else False
    
    def mutante_diagonal2(self):
        diagonales = []
        for fi in range(len(self.ADN)):
            diagonal = []
            for cl in range(len(self.ADN)):
                fila = fi + cl
                if fila < len(self.ADN):
                    diagonal.append(self.ADN[cl][fila])
                if len(diagonal) >= (6 - fi) and fi <= 2:
                    palabra = ''.join(diagonal)
                    diagonales.append(palabra)
                    diagonal = []                
        self.mutantes_encontrados += self.verificador(diagonales)
        return True if self.verificador(diagonales) == 1 else False

            # atatat,agagag,acacac,atatat,agagag,acacac

            # tatttt,ggaggg,cccacc,ttttat,ggggga,cccccc

            # ttattt,gggagg,ccccac,ttttta,ggggga,ccccca

            # tttttt,aggggg,cacccc,ttattt,gggagg,ccccac     

            # tttttt,gggggg,accccc,tatttt,ggaggg,cccacc

            # ttttta,ggggag,cccacc,ttattt,gagggg,accccc
    def invertir_matriz(ADN):
        arreglo = []
        matriz_invertida = []
        for i in range(len(ADN)):
            palabra = ADN[i]
            for j in range(len(ADN)-1, -1, -1):
                arreglo.append(palabra[j])
        for i in range(0,len(arreglo), 6):
            arreglo = arreglo[i:i + 6]
            palabra = ''.join(palabra)
            matriz_invertida.append(palabra)
        return matriz_invertida 
        
    def verificador(self, ADN):
        for i in range(len(ADN)):
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

    def mostrar_menu(self):
        print("""
        Seleccionar el tipo de mutante que desea crear:
        1)- Radiación
        2)- Virus
        3)- Salir
        """)
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
        print(self.base_nitrogenada)
        self.posicion_horizontal = 0
        self.posicion_vertical = 0
        self.tipo_radiacion = "" 
        self.indicar_tipo_radiacion()
        self.indicar_posiciones()
        self.crear_mutante(self.base_nitrogenada, self.tipo_radiacion, self.posicion_vertical) if self.tipo_radiacion == "H" else self.crear_mutante(self.bases_nitrogenadas, self.tipo_radiacion, self.posicion_horizontal)

    def indicar_tipo_radiacion(self):
        while True:
            self.tipo_radiacion = input("Ingrese el tipo de radiacion ('V' vertical) o ('H' horizontal):\n").upper()
            print(self.tipo_radiacion)
            if self.tipo_radiacion == "H" or self.tipo_radiacion == "V":
                break
            else:
                print("Se ingreso una opcion invalida")

    def indicar_posiciones(self):
        condicion = True
        while condicion:
            self.posicion_horizontal = int(input("Ingrese la posicion horizontal donde desea que comience el mutante:\n"))
            self.posicion_vertical = int(input("Ingrese la posicion vertical donde desea que comience el mutante:\n"))
            print(self.tipo_radiacion)
            if self.tipo_radiacion == "H":
                print(self.posicion_vertical)
                if self.posicion_vertical > 2: 
                    print("Debido a que el largo de los mutante es de 4, no es compatible la posicion vertical ingresada")
                else: 
                    condicion = False
            else:
                if self.posicion_horizontal > 2: print("Debido a que el largo de los mutante es de 4, no es compatible la posicion horizontal ingresada")
                else: break

    def crear_mutante(self, base_nitrogenada:str, orientacion:str, posicion_inicial:int):
        posicion = posicion_inicial
        if orientacion == "H":
            self.radiacion_horizontal(base_nitrogenada,posicion)
        else:
            self.radiacion_vertical(base_nitrogenada, posicion)

    def radiacion_horizontal(self, celula_nitrogenada:str, posicion_inicial:int):
        tope = 0 
        palabra = list(self.ADN[self.posicion_horizontal])
        for i in range(posicion_inicial, len(palabra)):
            palabra[i] = celula_nitrogenada
            tope += 1
            if tope == 4: break
        palabra = ''.join(palabra)
        self.ADN[self.posicion_horizontal] = palabra
        print(self.ADN)

    def radiacion_vertical(self, celula_nitrogenada:str, posicion_inicial:int):
        tope = 0 
        for i in range(posicion_inicial, len(self.ADN)):
            palabra = list(self.ADN[i])
            palabra[self.posicion_vertical] = celula_nitrogenada
            tope += 1
            palabra = ''.join(palabra)
            self.ADN[i] = palabra
            if tope == 4: break
        print(self.ADN)

class Virus(Mutador):
    def __init__(self, ADN):
        super().__init__(ADN)
        self.posicion_horizontal = 0
        self.posicion_vertical = 0
        self.tipo_virus = ""
        self.definir_tipo_virus()
        self.definir_posicion()
        print(self.posicion_vertical)
        self.crear_mutante(self.base_nitrogenada, self.posicion_vertical)

    def definir_tipo_virus(self):
        print("""
            Seleccione la direccion del virus:
            1)- Izquierda a derecha
            2)- Derecha a izquierda
            """)
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
        self.virus_diagonal(posicion_inicial, base_nitrogenada) if self.tipo_virus == "Normal" else self.virus_diagonal_invertida(posicion_inicial, base_nitrogenada)

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
        print(self.ADN)
    
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
        print(self.ADN)

class Sanador:
    def __init__(self, ADN, ADN_invertido):
        self.ADN = ADN
        self.bases_nitrogenadas = ["A","C","G","T"]
        self.ADN_invertido = ADN_invertido
        self.detectar_mutantes()
        self.crear_ADN(self.bases_nitrogenadas)
        self.mostrar_ADN_sano()

    def detectar_mutantes(self):
        detector = Detector(self.ADN, self.ADN_invertido)
        return True if detector.detectar_mutantes() == True else False
    
    def crear_ADN(self, bases_nitrogenadas:list):
        if self.detectar_mutantes() == True:
            while self.detectar_mutantes() == True:
                for i in range(0, 6):
                    palabra = list(self.ADN[i])
                    for j in range(len(palabra)):
                        palabra[j] = random.choice(bases_nitrogenadas)
                    palabra = ''.join(palabra)
                    self.ADN[i] = palabra
                self.ADN_invertido = Detector.invertir_matriz(self.ADN)
                self.detectar_mutantes()
            return self.ADN
        else: return self.ADN

    def mostrar_ADN_sano(self):
        print(f"El ADN sanado se muestra a continuacion: {self.ADN}")