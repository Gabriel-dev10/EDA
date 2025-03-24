def Funcao(x):
    return x**3 - x - 2

def bissecao (a, b):
    while True:
        PontoMedio = (a + b ) / 2 
        if Funcao(PontoMedio) == 0:
            return PontoMedio
        elif Funcao(a) * Funcao(PontoMedio) < 0:
            b = PontoMedio 
        else:
            a = PontoMedio

a = float(input("Insira o maior valor do intervalo:"))

b = float(input("Insira o menor valor do intervalo:"))

