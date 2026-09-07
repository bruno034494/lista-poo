#variavel para receber valores e contagem de valor
frase = input("qual eh a frase?")
palavras = frase.split()
cotagem = {}
#codição para saber a contagem
for p in palavras:
    if p in cotagem:
        cotagem[p] += 1
    else:
        cotagem[p] = 1
#siada de valores        
for chave,valor in cotagem.items():
    print(f"a palavra {chave} e a quantidade {valor}")
