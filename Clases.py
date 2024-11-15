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
        diagonales = {}    
        

        for cl in range(len(ADN)):
            numero_arreglo = 0
            diagonal = []
            for fila in range(len(ADN)):
                columna = cl + fila
                if columna < len(ADN):
                    diagonal.append(ADN[fila][columna])
                    if len(diagonal) >= (6 - cl) and cl <= 2:
                        diagonales[numero_arreglo] = diagonal
                        numero_arreglo += 1
                        numero_arreglo + 1 if numero_arreglo == 3 else 0
                        diagonal = []
        mutante += Detector.verificador(diagonales)

        for fi in range(len(ADN)):
            numero_arreglo = 0
            diagonal = []
            for cl in range(len(ADN)):
                fila = fi + cl
                if fila < len(ADN):
                    diagonal.append(ADN[fila][cl])
                if len(diagonal) >= (6 - fi) and fi <= 2:
                    diagonales[numero_arreglo] = diagonal
                    numero_arreglo += 1
                    diagonal = []                
        mutante += Detector.verificador(diagonales)

        if mutante >= 1:
            return True
        else:
            return False

            # attttt,gaaggg,ccaacc,tttaat,ggggaa,ccccca

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
        print(matriz_invertida)
        return matriz_invertida 
        
    def verificador (diagonales):
        encontrar_mutante = 0
        for i in range(len(diagonales)):
            diagonal = diagonales[i]
            for j in range(0,len(diagonal)):
                if j == 0:
                    encontrar_mutante +=1 if diagonal[j] == diagonal[j+1] else 0
                elif j != 6:
                    encontrar_mutante +=1 if diagonal[j] == diagonal[j-1] else 0
        return encontrar_mutante
