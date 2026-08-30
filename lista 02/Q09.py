notas = []
while len(notas) < 5:
    try:
        nota = float(input(f"Qual é sua {len(notas) + 1}ª nota? "))
        notas.append(nota)
    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite um número.")

media=sum(notas)/len(notas)
maior=max(notas)
menor =min(notas)
print(notas)
print(f"sua media eh {media:.2f} ")
print(f"a maior nota eh{maior}")
print(f"sua menor nota eh {menor}")

