def fatorar(numero):
    resultado = 1
    for i in range(numero, 1, -1):
        resultado = resultado * i
        print(f'{resultado}')

numero = int(input('Digite um número para fatorar: '))

fatorar(numero)