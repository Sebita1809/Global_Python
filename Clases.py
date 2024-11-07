class Detector:
    ADN = []
    def __init__(self, nombre, ADN):
        self.nombre = nombre
        self.ADN = ADN
    
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
        diagonal = []
        encontrar_mutante = 0
        for columna in range(0, int(len(ADN)/2)):
            #aaaaaa,gggggg,cccccc,tttttt,gggggg,cccccc
            for fila in range(0, (len(ADN))):
                if columna == 0:
                    diagonal.append(ADN[fila][fila])
                    if diagonal[fila][fila] == 
                    if len(diagonal) == 6:
                        print(diagonal)
                        diagonal = []
                elif columna == 1:
                    if fila == 0:
                        diagonal.append(ADN[fila][columna])
                    else:
                        diagonal.append(ADN[fila][columna+1])
                    if len(diagonal) == 5:
                        print(diagonal)
                        diagonal = []
                        break
                else:
                    if fila == 0:
                        diagonal.append(ADN[fila][columna])
                    else:
                        diagonal.append(ADN[fila][columna+1])
                    if len(diagonal) == 4:
                        print(diagonal)
                        break
        


        ##return True if mutante > 0 else False