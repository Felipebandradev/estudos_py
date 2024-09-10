# Estudos sobre Python

Em python tudo precisa ser bem identado para evitar erros e deixar mais legivel

> Sintaxe limpa: linguagem fácil de aprender

> Alto Nível

> Instalavel na máquina

> Interpretada: executa o código fonte > executa linha a linha.

> Execução IDE

## Código

> criação de varíaveis e comentários

```py
# (#)-> utilizado para documentar/anotar coisas no código

# Declarando uma varíavel
num = 10
```

> Funções: tarefas para fazer algo, são instruções ou subgramas

```py
# Exibição na tela
print('Exibindo na tela')

# Pedindo para usuário informar um dado input()
numero = input('Informe um número: ')
# o dado retornado no input() é uma string/texto

# Conversão do tipo de dado para inteiro int()
numero = int( input('Informe um número'))

# Criando uma função sem parâmetros
def bemvindo():
    print('Bem-Vindo')

bemvindo() # chamada da função

# Criando uma função com parâmetros
def bemvindo(nome):
    print(f'Boas Vindas: {nome}') # f = formater string

bemvindo("Nome") # chamda da função e passando um parâmetro

```

> Condicionais

```py
# Simples
media = int( input('Digite sua média: '))

if media >= 7:
    print('Aprovado')
else:
    print('Reprovado')

# Com else if

if media >= 7:
    print('Aprovado')
elif media > 4 and media < 7:
    print('Recuperação')
else:
    print('Reprovado')

```

> Laços de repetição: facilita o desenvolvedor a escrever menos

```py
numero = int(input('Digite um número'))

# estrutura do for(para)
for contador in range(1,numero + 1):
    print(contador)

# estrutura do while(enquanto)
# inicializando a varíavel de controle do loop
controle = 1

while controle <= numero:
    print(controle)
    # incrementando a varíavel de controle para não criar um loop infinito
    controle = controle + 1

```

- ## Bubble Sort(Algoritmo de ordenação)

O algoritmo vai comparar cada número para trocar as posições dos elementos em uma determinada situação

```py
for i in range(n - 1):
    for i in range(n - 1):
        # comparando os itens
        if lista[i] > lista[i+1]:
            #trocando de posição os elementos da lista
            lista[i], lista[i+1] = lista[i+1], lista[i]

```

## Bibliotecas

Bibliotecas de programação são recursos que ajudam a escrever o código

- > Tkinter ( interface )

  ```py
  # importando a biblioteca e apelidandando (as)
  import tkinter as tk

  # crianção da janela
  janela = tk.Tk()

  #especificar o tamanho da janela definida em pixel
  janela.geometry('400x400')

  # caixa de entrada de dados 01
  campo1 = tk.Entry (janela)

  # exibir na janela
  campo1.pack(padx=10, pady=20)

  #Botão de ação
  botao = tk.Button(janela, text='+', command=soma )

  # Definindo a localização/posicionamento dentro da janela em px
  botao.place(x=120, y=120)

  #vinculando a variavel numero com entry
  num1 = float(campo1.get())

  # Alterando os parâmetros de uma função
  total.config(text=f'Alterando o texto')


  # loop principal da interface grafica rodar em loop
  janela.mainloop()


  ```
