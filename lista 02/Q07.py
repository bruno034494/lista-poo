notas = []
print("--- Sistema de Notas ---")
print("Dica: Aperte 'Enter' sem digitar nenhum número para finalizar o cadastro.\n")
while True:
    entrada = input("Digite uma nota: ")
    
    if entrada == "":
        break
    notas.append(float(entrada))
try:
    media = sum(notas) / len(notas)
    print(f"\nSucesso! Foram cadastradas {len(notas)} notas.")
    print(f"A média final do estudante é: {media:.2f}")
except ZeroDivisionError:
    print("\nErro de Operação: Nenhuma nota foi inserida. Impossível realizar divisão por zero.")
# CÓDIGO FEITO POR: BRUNO DE SOUZA BUENO