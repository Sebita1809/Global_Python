import random
from funciones import *
print("Hola munddo")

## CLASE DETECTOR:
## - Esta clase recibe un ADN (que es una lista) y retorna True si ha encontrado mutantes o False en el caso contrario
class Detector:
    def __init__(self, ADN:list):
        try:
            if not ADN:
                raise ValueError
            self.ADN = ADN
            self.ADN_invertido = invertir_matriz(self.ADN)
            self.mutantes_encontrados = 0
            self.detectar_mutantes(self.ADN)
            print(self.detectar_mutantes(self.ADN))
        except ValueError:
            print(f"Recuerde que debe ingresar un ADN primero")

    def detectar_mutantes(self, ADN:list):
        self.mutante_horizontal(ADN)
        self.mutante_vertical(ADN)
        self.mutante_diagonal1(ADN)
        self.mutante_diagonal2(ADN)
        self.mutante_diagonal_inversas(ADN)
        return True if self.mutantes_encontrados > 0 else False

## La funcion MUTANTE_HORIZONTAL envia el ADN a un verificador
    def mutante_horizontal(self, ADN:list):
        return True if self.verificador(ADN) == 1 else False

## Esta funcion genera un lista, donde cada palabra("fila") está conformada por las columnas del ADN, luego se las envia al verificador
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

## La funcion MUTANTE_DIAGONAL1 se encarga de generar una lista, donde cada palabra("fila") está conformada
## por las diagonales y luego se las pasa al verificador. Las diagonales que lo conforman son:
## D D D A A A
## A D D D A A
## A A D D D A
## A A A D D D
## A A A A D D
## A A A A A D
## Solo nos enfocamos en esas diagonales porque son las unicas donde puede repetirse 4 veces o mas una base nitrogenada (mutante)
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

## La funcion MUTANTE_DIAGONAL2 se encarga de generar una lista, donde cada palabra("fila") está conformada
## por las diagonales y luego se las pasa al verificador. Las diagonales que lo conforman son:
## D A A A A A
## D D A A A A
## D D D A A A
## A D D D A A
## A A D D D A
## A A A D D D
## Solo nos enfocamos en esas diagonales porque son las unicas donde puede repetirse 4 veces o mas una base nitrogenada (mutante)
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

## La funcion MUTANTE_DIAGONAL_INVERSA se encarga de invertir la matriz (con la funcion INVERTIR_MATRIZ) lo que
## permite que despues podamos enviale ese ADN invertido a las funciones diagonales anteriores y verificar las
## diagonales secundarias. Estas serian las diagonales secundarias:
## A A A D D D
## A A D D D D
## A D D D D D
## D D D D D A
## D D D D A A
## D D D A A A
    def mutante_diagonal_inversas(self, ADN:list):
        self.mutante_diagonal1(invertir_matriz(ADN))
        self.mutante_diagonal2(invertir_matriz(ADN))

## La funcion VERIFICADOR recibe una lista (que serian los ADN o listas creadas por los componenetes del ADN)
## y verifica que no se encuentren mutantes (base nitrogenada repetida 4 o mas veces).
    def verificador(self, ADN):
        encontrar_mutante = 0
        for i in range(len(ADN)):
            encontrar_mutante = 0
            palabra = ADN[i]
            for j in range(0,len(palabra)-1):
                encontrar_mutante +=1 if palabra[j] == palabra[j+1] else 0
            if encontrar_mutante >=3:
                break
        return 1 if encontrar_mutante >= 3 else 0

## CLASE MUTADOR:
## - Esta clase recibe el ADN y funciona como padre para las clases VIRUS y RADIACION. En esta clase, tambien se
## le pregunta al usuario que tipo de mutacion desea realizar
class Mutador:
    def __init__(self, ADN):
        self.ADN = ADN
        self.base_nitrogenada = random.choice(["A","C","G","T"])

## Funcion que herederá a las clases hijas
    def crear_mutante(self):
        pass

## Esta funcion, llama a la funcion MOSTRAR_MENU_MUTADOR, para mostrarle el menu al ususario y que este seleccione
## el tipo de mutacion que desea realizar
    def registrar_respuesta(self):
        mostrar_menu_mutador()
        respuesta = int(input("Ingrese su respuesta:\n"))
        if respuesta == 1:
            Radiacion(self.ADN)
        elif respuesta == 2:
            Virus(self.ADN)
        elif respuesta == 3:
            print("Saliendo...")

## CLASE RADIACION:
## - Esta clase es hija de la clase MUTADOR, por lo que va a heredar sus atributos y metodos
## - En esta clase se van a introducir mutantes de manera vertical u horizontal (según desee el usuario) y
## se va retornar el ADN resultante
class Radiacion(Mutador):
    def __init__(self, ADN):
            try:
                if not ADN:
                    raise ValueError
                super().__init__(ADN)
                self.posicion_horizontal = 0
                self.posicion_vertical = 0
                self.tipo_radiacion = "" 
                self.base_nitrogenada = self.base_nitrogenada
                self.indicar_tipo_radiacion()
                self.indicar_posiciones()
                self.crear_mutante(self.base_nitrogenada, self.tipo_radiacion, self.posicion_vertical) if self.tipo_radiacion == "H" else self.crear_mutante(self.base_nitrogenada, self.tipo_radiacion, self.posicion_horizontal)
            except ValueError:
                print("Recuerde que debe ingresar un ADN primero")

## Esta funcion se encarga de determinar si los mutantes a insertar van a ser verticales u horizontales
    def indicar_tipo_radiacion(self):
        while True:
            self.tipo_radiacion = input("Ingrese el tipo de radiacion ('V' vertical) o ('H' horizontal):\n").upper()
            if self.tipo_radiacion == "H" or self.tipo_radiacion == "V":
                break
            else:
                print("Se ingreso una opcion invalida")

## Esta funcion se encarga de determinar las posiciones verticales y horizontales en las cuales insertará el mutante
    def indicar_posiciones(self):
        while True:
            self.posicion_horizontal = int(input("Ingrese la posicion horizontal donde desea que comience el mutante:\n"))
            self.posicion_vertical = int(input("Ingrese la posicion vertical donde desea que comience el mutante:\n"))
            self.indicar_posiciones() if verificar_posiciones(self.posicion_horizontal, self.posicion_vertical) == True else None
            if self.tipo_radiacion == "H":
                if self.posicion_vertical > 3: 
                    print("Debido a que el largo de los mutante es de 4, no es compatible la posicion vertical ingresada")
                else: 
                    break
            elif self.tipo_radiacion == "V":
                if self.posicion_horizontal > 3: print("Debido a que el largo de los mutante es de 4, no es compatible la posicion horizontal ingresada")
                else: break

## La funcion CREAR_MUTANTE se encarga de mostrar el ADN con mutante insertados. Este ADN será diferente,según
## la direccion que el usuario haya elegido (vertical u horizontal)
    def crear_mutante(self, base_nitrogenada:str, orientacion:str, posicion_inicial:int):
        if orientacion == "H":
            print(self.radiacion_horizontal(base_nitrogenada,posicion_inicial))
        else:
            print(self.radiacion_vertical(base_nitrogenada, posicion_inicial))

## Esta es la funcion encargada de insertar los mutantes de manera horizontal
    def radiacion_horizontal(self, celula_nitrogenada:str, posicion_inicial:int):
        tope = 0 
        palabra = list(self.ADN[self.posicion_horizontal - 1])
        for i in range((posicion_inicial - 1), len(palabra)):
            palabra[i] = celula_nitrogenada
            tope += 1
            if tope == 4: break
        palabra = ''.join(palabra)
        self.ADN[self.posicion_horizontal - 1] = palabra
        return self.ADN

## Esta es la funcion encargada de insertar los mutantes de manera vertical
    def radiacion_vertical(self, celula_nitrogenada:str, posicion_inicial:int):
        tope = 0 
        for i in range((posicion_inicial - 1), len(self.ADN)):
            palabra = list(self.ADN[i])
            palabra[(self.posicion_vertical - 1)] = celula_nitrogenada
            tope += 1
            palabra = ''.join(palabra)
            self.ADN[i] = palabra
            if tope == 4: break
        return self.ADN

## CLASE VIRUS:
## - Esta clase es hija de la clase MUTADOR, por lo que va a heredar sus atributos y metodos
## - En esta clase se van a introducir mutantes de manera diagonal y finalmente se retornaré el ADN resultante
class Virus(Mutador):
    def __init__(self, ADN):
        try:
            if not ADN:
                raise ValueError
            super().__init__(ADN)
            self.posicion_horizontal = 0
            self.posicion_vertical = 0
            self.tipo_virus = ""
            self.base_nitrogenada = self.base_nitrogenada
            self.definir_tipo_virus()
            self.definir_posicion()
            self.crear_mutante(self.base_nitrogenada, self.posicion_vertical)
        except ValueError:
            print("Recuerde que debe ingresar un ADN primero")

## Esta funcion va a determinar si el mutante a insertar va a ser en las diagonales normales o en las invertidas/secundarias
    def definir_tipo_virus(self):
        mostrar_menu_virus()
        respuesta = int(input("Ingrese su respuesta:\n"))
        if respuesta == 1 or respuesta == 2:
            self.tipo_virus = "Normal" if respuesta == 1 else "Invertido"
        else:
            print("La opcion ingresada no es valida")
            self.definir_tipo_virus()

## Esta funcion determinará las posiciones en las que se deberá empezar a insertar el mutante. Según el tipo
## de diagonal a insertar, las posiciones a definir serán diferentes y deberan cumplir ciertos parametros:
## D D D A A A                      A A A D D D
## D D D D A A      Posiciones:     A A D D D D      Posiciones:
## D D D D D A  --> col: max 3      A D D D D D  --> col: min 3
## A D D D D D      fil: max 3      D D D D D A      fil: nin 3
## A A D D D D                      D D D D A A
## A A A D D D                      D D D A A A
    def definir_posicion(self):
        print("Desde que posicion vertical desea empezar el virus?")
        self.posicion_vertical = int(input("Ingrese la posicion:\n"))
        print("Desde que posicion horizontal desea empezar el virus?")
        self.posicion_horizontal = int(input("Ingrese la posicion:\n"))
        if self.posicion_horizontal > 2 or self.posicion_vertical > 2:
            if self.tipo_virus == "Normal":
                print("Debido a que los virus tienen una longitud de 4, las posiciones no pueden excederse de 2")
                self.definir_posicion()
        else: 
            if self.tipo_virus == "Invertido":
                print("Debido a que los virus tienen una longirud de 4, las posiciones no pueden ser menor de 3")
                self.definir_posicion()

## La funcion CREAR_MUTANTE se encarga de mostrar el ADN con las mutaciones insertadas de manera diagonal, dependiendo
## del tipo de virus (si es en las diagonales normales o invertias/secundarias) el ADN será diferente
    def crear_mutante(self, base_nitrogenada:str, posicion_inicial:int):
            print(self.virus_diagonal(posicion_inicial, base_nitrogenada)) if self.tipo_virus == "Normal" else print(self.virus_diagonal_invertida(posicion_inicial, base_nitrogenada))

## Esta funcion es la encargada de insertar los mutantes en las diagonales
    def virus_diagonal(self, posicion_vertical:int, base_nitrogenada:str):
        tope = 0
        aumento = 1
        for i in range((self.posicion_horizontal - 1), (len(self.ADN)-1)):
            palabra = list(self.ADN[i])
            if i == self.posicion_horizontal - 1:
                palabra[posicion_vertical - 1] = base_nitrogenada  
            else: 
                palabra[(posicion_vertical - 1) + aumento] = base_nitrogenada
                tope += 1
                palabra = ''.join(palabra)
                self.ADN[i] = palabra
                if tope == 4: break
        return self.ADN

## Esta funcion es la encargada de insertar los mutantes en las diagonales invertidas o secundarias
    def virus_diagonal_invertida(self, posicion_vertical:int, base_nitrogenada:str):
        tope = 0
        aumento = 1
        for i in range((self.posicion_horizontal - 1), (len(self.ADN)-1)):
            palabra = list(self.ADN[i])
            if i == self.posicion_horizontal - 1:
                palabra[posicion_vertical - 1] = base_nitrogenada 
            else:
                palabra[(posicion_vertical - 1) -aumento] = base_nitrogenada
                aumento += 1
            tope += 1
            palabra = ''.join(palabra)
            self.ADN[i] = palabra
            if tope == 4: break
        return self.ADN

## CLASE SANADOR:
## - Esta clase recibe como parametro un ADN y debe verificar si posee o no mutantes
## - Esta debe retornar un ADN sanado en caso de que hayan mutantes o el mismo ADN en el caso de que no hayan
class Sanador:
    def __init__(self, ADN:list):
        try:
            if not ADN:
                raise ValueError
            self.bases_nitrogenadas = ["A","C","G","T"]
            self.ADN = ADN
            self.ADN_invertido = invertir_matriz(self.ADN)
            self.detectar_mutantes(self.ADN)
            self.sanar_mutantes(self.ADN)
            self.mostrar_ADN_sano()
        except ValueError:
            print(f"Recuerde que debe ingresar un ADN primero")

## Esta funcion se encarga de enviarle el ADN existente o creado, a la clase DETECTOR para que
## en esta misma, se analice si contiene o no mutantes. Depediendo de si hay o no, se retorna True o False
    def detectar_mutantes(self, ADN:list):
        detector = Detector(ADN)
        return True if detector.detectar_mutantes(ADN) == True else False

## La funcion SANAR_MUTANTE se encarga de crear ADN aleatorios, para luego ser enviado a la funcion
## DETECTAR_MUTANTES para que este indique si tienen mutante o no, en caso de contener, se genera otro ADN
## y se repite con el mismo proceso. Si el ADN no contiene mutantes, se retorna
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

## Esta funcion se encarga de mostrar por pantalla al ADN sanado (sin mutantes)
    def mostrar_ADN_sano(self):
        print(f"El ADN sanado se muestra a continuacion: {self.sanar_mutantes(self.ADN)}")

## ---
