import numpy as np
import matplotlib.pyplot as plt


def Equacao1(x):
    return 0.5 * x + 0.5


def Equacao2(x):
    return -x + 2


IntersecaoX = 1
IntersecaoY = Equacao1(IntersecaoX)  


ValorX = np.linspace(-10, 10, 400)
ValorY_Equacao1 = Equacao1(ValorX)
ValorY_Equacao2 = Equacao2(ValorX)

plt.figure(figsize=(8, 6))
plt.plot(ValorX, ValorY_Equacao1, label="y = 0.5x + 0.5", color="Purple")
plt.plot(ValorX, ValorY_Equacao2, label="y = -x + 2", color="Cyan")


plt.scatter(IntersecaoX, IntersecaoY, color="green", zorder=5)
plt.text(IntersecaoX + 0.5, IntersecaoY, f'({IntersecaoX:.2f}, {IntersecaoY:.2f})', fontsize=12)


plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.title("Sistema de Equações Lineares")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()


plt.show()

print(f"Ponto de interseção: x = {IntersecaoX:.2f}, y = {IntersecaoY:.2f}")
