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
print()
b = float(input("Insira o menor valor do intervalo:"))
print()

if Funcao(a) * Funcao(b) > 0:
    print("Não há raízes neste intervalo.")
else:
    raiz = bissecao(a, b)
    print(f"A raiz aproximada é: {raiz}")