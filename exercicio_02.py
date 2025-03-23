a = 2
b = 2
c = -6


delta = b * b - 4 * a * c

if delta >= 0:
    x1 = (-b + delta**0.5) / (2 * a)
    x2 = (-b - delta**0.5) / (2 * a)
    print(f"As raízes da equação são: {x1} e {x2}")
else:
    print("Não existem raízes reais.")
