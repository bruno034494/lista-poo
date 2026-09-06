continuar = 's'
while continuar.lower() == 's':
    print("\n--- CONVERSOR DE TEMPERATURA ---")
    temperatura = float(input("Informe a temperatura: "))
    
    print("1 - Converter de Celsius para Fahrenheit")
    print("2 - Converter de Celsius para Kelvin")
    opcao = input("Escolha a conversão (1 ou 2): ")
    
    if opcao == '1':
        resultado = (temperatura * 1.8) + 32
        print(f"> {temperatura}°C equivalem a {resultado:.2f}°F")
    elif opcao == '2':
        resultado = temperatura + 273.15
        print(f"> {temperatura}°C equivalem a {resultado:.2f}K")
    else:
        print("> Opção inválida.")
        
    continuar = input("\nDeseja realizar uma nova conversão? (s/n): ")
# CÓDIGO FEITO POR: BRUNO DE SOUZA BUENO