numero =  int(input("Digite um número de 1 a 10: "))

if numero <= 10:
    for contador in range(1,11):
        print( numero,"X",contador,"=",numero*contador)
else:
    print("Valor",numero,"invalido tabuada do 1 ao 10")