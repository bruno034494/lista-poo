a = float(input("qual e seu coificiente a"))
b = float(input("qual e seu coificiente b"))
c = float(input("qual e seu coificiente c"))
delta = (b**2)/ (4*a*c)
if delta < 0:
    print("Não há raízes reais.")
elif delta == 0:
    raiz = -b / (2 * a)
    print(f"Há apenas uma raiz real: {raiz:.2f}")
else:
    raiz1 = (-b + (delta ** 0.5)) / (2 * a)
    raiz2 = (-b - (delta ** 0.5)) / (2 * a)
    print(f"As duas raízes reais são: {raiz1:.2f} e {raiz2:.2f}")