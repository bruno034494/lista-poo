def calcular_rotina(valor1, valor2):
    produto = valor1 * valor2
    
    if produto <= 1000:
        print(f"Produto: {produto} -> Produto menor ou igual a 1000")
        return produto
    else:
        soma = valor1 + valor2
        print(f"Soma: {soma} -> Produto ultrapassou 1000")
        return soma
numero1 = int(input("Digite o primeiro valor: "))
numero2 = int(input("Digite o segundo valor: "))

calcular_rotina(numero1, numero2)

# CÓDIGO FEITO POR: BRUNO DE SOUZA BUENO