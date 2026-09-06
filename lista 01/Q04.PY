
escolha = int(input("Digite 1 para calcular a hipotenusa ou 2 para calcular o cateto: "))
if escolha == 1:
    print("Você vai calcular a hipotenusa!")
    l1 = float(input("Qual é o valor do cateto 1? "))
    l2 = float(input("Qual é o valor do cateto 2? "))
    # Fórmula: h = √(c1² + c2²)
    calcular = (l1**2 + l2**2)**(1/2)
    print(f"O valor da hipotenusa é: {calcular:.2f}")
elif escolha == 2:
    print("Você vai calcular o cateto!")
    lh = float(input("Qual é o valor da hipotenusa? "))
    lc = float(input("Qual é o valor do cateto conhecido? "))
    # Fórmula: c = √(h² - c²)
    calcular = (lh**2 - lc**2)**(1/2)
    print(f"O valor do cateto é: {calcular:.2f}")
else:
    print("Opção inválida! Digite 1 ou 2.")
# CODIGO FEITO POR: BRUNO DE SOUZA BUENO