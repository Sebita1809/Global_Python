class Detector:
    ADN = []
    def __init__(self, nombre, ADN):
        self.nombre = nombre
        self.ADN = ADN
        self.mutante = 0
        self.mutante_H = self.mutante_horizontal()
        self.mutante_V = self.mutante_vertical()
        self.mutante_D = self.mutante_diagonal1()
        self.mutante_D2 = self.mutante_diagonal2()
        print(self.mutante_H)
        print(self.mutante_V)
        print(self.mutante_D)
        print(self.mutante_D2)
        print(self.mutante)
        self.verificador()

    
    def mutante_horizontal(self):
        ADN = self.ADN
        self.mutante += self.verificador(ADN)
        return True if self.verificador(ADN) == 1 else False
    
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
        self.mutante += self.verificador(columnas)
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
        self.mutante += self.verificador(diagonales)
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
        self.mutante += self.verificador(diagonales)
        return True if self.verificador(diagonales) == 1 else False

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
        
    def verificador(self, ADN):
        for i in range(len(ADN)):
            encontrar_mutante = 0
            palabra = ADN[i]
            for j in range(0,len(palabra)-1):
                encontrar_mutante +=1 if palabra[j] == palabra[j+1] else 0
            if encontrar_mutante >=3:
                break
        return 1 if encontrar_mutante >= 3 else 0
