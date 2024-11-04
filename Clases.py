class Detector:
    ADN = []
    def __init__(self, nombre, ADN):
        self.nombre = nombre
        self.ADN = ADN
        print(self.nombre)
        print(self.ADN)
    
    def mutante_horizontal(ADN):
        print(ADN)
        mutante = 0
        encontrar_mutante = 0
        for i in range(0 , len(ADN)):
            palabra = ADN[i]
            for j in range(0, len(ADN)-1):
                incremento = 1
                if palabra[j] == palabra[incremento]:
                    print(palabra[j])
                    encontrar_mutante += 1
                else:
                    encontrar_mutante = 0
                incremento += 1
                mutante = 1 if encontrar_mutante >= 4 else 0
        return True if mutante > 0 else False
    
    def mutante_vertical(ADN):
        mutante = 0
        columna = []
        encontrar_mutante = 0
        for i in range(0 , len(ADN)):
            columna.append(ADN[i][i])
            if len(columna) == 6:
                for j in range(0, len(columna)-1):
                    incremento = 1
                    if columna[j] == columna[j+1]:
                        encontrar_mutante += 1
                    else:
                        encontrar_mutante = 0
                    incremento += 1
                    mutante = 1 if encontrar_mutante >= 4 else 0
        return True if mutante > 0 else False

