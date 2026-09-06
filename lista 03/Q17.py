vogais = "aeiou"
qtdvogais = 0
qtdconsoantes = 0

print("--- CLASSIFICADOR DE CARACTERES ---")
for i in range(10):
    letra = input(f"Informe a {i+1}ª letra: ").lower()
    if letra.isalpha():
        if letra in vogais:
            qtdvogais += 1
        else:
            qtdconsoantes += 1
print(f"\nQuantidade de vogais: {qtdvogais}")
print(f"Quantidade de consoantes: {qtdconsoantes}")

# CÓDIGO FEITO POR: BRUNO DE SOUZA BUENO