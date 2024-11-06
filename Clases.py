class Detector:
    ADN = []
    def __init__(self, nombre, ADN):
        self.nombre = nombre
        self.ADN = ADN
        print(self.nombre)
        print(self.ADN)
    
    def mutante_horizontal(ADN):
        mutante = 0
        encontrar_mutante = 0
        for i in range(0 , len(ADN)):
            palabra = ADN[i]
            for j in range(0, len(ADN)-1):
                incremento = 1
                if palabra[j] == palabra[incremento]:
                    encontrar_mutante += 1
                else:
                    encontrar_mutante = 0
                incremento += 1
                mutante += 1 if encontrar_mutante >= 4 else 0
        return True if mutante > 0 else False
    
    def mutante_vertical(ADN):
        mutante = 0
        columna = []
        encontrar_repeticiones = 0
        for x in range(0, len(ADN)):
            for i in range(0 , len(ADN)):
                columna.append(ADN[i][x])
                if len(columna) == 6:
                    print(columna)
                    for j in range(0, len(columna)-1):
                        incremento = 1
                        if columna[j] == columna[incremento]:
                            encontrar_repeticiones += 1
                        else:
                            encontrar_repeticiones = 0
                        incremento += 1
                        mutante += 1 if encontrar_repeticiones >= 4 else 0
            columna = []
        return True if mutante > 0 else False
    

    def mutante_diagonal1(ADN):
        mutante = 0
        columna = []
        encontrar_repeticiones = 0
        incrementador = 0
        for x in range(0, len(ADN)):
            for i in range(0 , len(ADN)-1):
                if x==0:
                    columna.append(ADN[i][x])
                elif x<=3:
                    incrementador=x
                    columna.append(ADN[i][incrementador+1])
                    incrementador+=1
                    print(incrementador)
                    if len(columna) == 6:
                        print(columna)
                        for j in range(0, len(columna)-1):
                            incremento = 1
                            if columna[j] == columna[incremento]:
                                encontrar_repeticiones += 1
                            else:
                                encontrar_repeticiones = 0
                            incremento += 1
                            mutante += 1 if encontrar_repeticiones >= 4 else 0
                else: break
            columna = []
        return True if mutante > 0 else False