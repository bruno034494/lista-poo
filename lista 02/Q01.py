soma = 0
qtd_validos = 0
print("Informe 10 códigos válidos (divisíveis por 6):")
while qtd_validos < 10:
    n = int(input(f"Qual é o seu código {qtd_validos + 1}? "))
    if n % 6 == 0:
        soma += n
        qtd_validos += 1 
    else:
        print("Erro: O número não é divisível por 6. Tente novamente.")
print("\nTodos os 10 códigos foram aceitos!")
print(f"O número somado é: {soma}")
# CÓDIGO FEITO POR: BRUNO DE SOUZA BUENO