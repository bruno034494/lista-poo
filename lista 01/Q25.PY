horas = float(input("Digite a quantidade de horas: "))
if horas >= 10 and horas <= 40:
    c = horas / 7
    print(f"\nPlano configurado com {horas} horas ")
    c = horas / 7
    print(f"\nIsso equivale a aproximadamente {c:.2f} horas por dia)")
elif horas < 10:
    print("Quantidade muito baixa.")
elif horas > 40:
    print("Quantidade muito alta.")
print("fim do programa")