hipotenusa = float(input("vc quer calcular  hipotenusa digete 1? "))
cateto = float(input("vc quer calcular  cateto digete 2? "))
if hipotenusa==1:
    l1 = float(input("qual e  o valor do cateto 1? "))
    l2 = float(input("qual e o cateto 2 do triangulo? "))
    calcular = (l1**2 + l2**2)**(1/2)
    print("o valor da hipotenusa é:", calcular)

elif cateto==2:
    print("você vai calcular o cateto! ")
    lh = float(input("qual e  o valor da hipotenusa? "))
    lc = float(input("qual e o cateto  do triangulo? "))
    calcular = (lh**2 + lc**2)**(1/2)
    print("o valor do cateto é:", calcular)
    
