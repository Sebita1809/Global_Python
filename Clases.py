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
        for columna in range(0, int(len(ADN)/2)):
            cl = columna
            # attttt,gaaggg,ccaacc,tttaat,ggggaa,ccccca

            # tatttt,ggaggg,cccacc,ttttat,ggggga,cccccc

            # ttattt,gggagg,ccccac,ttttta,ggggga,ccccca
            for fila in range(0, (len(ADN))):
                if columna == 0:
                    diagonal.append(ADN[fila][fila])
                    if len(diagonal) == 6:
                        mutante += Detector.verificador(diagonal)
                        print(diagonal)
                        print(mutante)
                        diagonal = []
                elif columna == 1:
                    if fila == 0:
                        diagonal.append(ADN[fila][columna])
                    else:
                        cl += 1
                        diagonal.append(ADN[fila][cl])
                    if len(diagonal) == 5:
                        print(diagonal)
                        mutante += Detector.verificador(diagonal)
                        print(mutante)
                        diagonal = []
                        break
                else:
                    if fila == 0:
                        diagonal.append(ADN[fila][columna])
                    else:
                        cl += 1
                        diagonal.append(ADN[fila][cl])
                    if len(diagonal) == 4:
                        print(diagonal)
                        mutante += Detector.verificador(diagonal)
                        print(mutante)
                        diagonal = []
                        break
        return True if mutante >= 1 else False
    
    def verificador (diagonal):
        encontrar_mutante = 0
        for i in range(0,len(diagonal)):
            if i == 0:
                encontrar_mutante +=1 if diagonal[i] == diagonal[i+1] else 0
            elif i != 6:
                encontrar_mutante +=1 if diagonal[i] == diagonal[i-1] else 0
        return encontrar_mutante