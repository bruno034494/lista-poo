soma = 0
d = {
    "progamação" : "",
    "banco de dados" :"",
    "Redes de computadores" :""
}
for chave,valor in d.items():
   valor=input(f"qual e a quantidade de horas da materia {chave} :")
   if valor.isdigit():#isdigit() serve para  verificar se todos os caracteres daquele texto são números
        horas = int(valor) 
        if horas >= 0:
            d[chave] = horas
            soma=soma+ horas
        else:
            print("Número inválido. As horas não podem ser negativas.")
print(soma)
# CÓDIGO FEITO POR: BRUNO DE SOUZA BUENO