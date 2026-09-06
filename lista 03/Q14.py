numero = int(input("Informe um número inteiro não negativo: "))
fatorial = 1

# O laço começa em 1 e vai até o número digitado
for i in range(1, numero + 1):
    fatorial *= i
    
print(f"O fatorial de {numero} é {fatorial}.")
# CÓDIGO FEITO POR: BRUNO DE SOUZA BUENO