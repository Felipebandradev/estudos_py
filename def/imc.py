def imc(peso, altura):
   calculo = peso/(altura**2)
   print(f'imc: {calculo:.2f}')

peso = float(input('Digite o peso: '))
altura = float(input('Digite a altura: '))

imc(peso, altura)