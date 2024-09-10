# importando a biblioteca de criação de janela
import tkinter as tk

#Criando a função que soma os números
def soma():
    #vinculando a variavel numero com entry
    num1 = float(campo1.get())
    num2 = float(campo2.get())

    resultado = num1 + num2
    total.config(text=f'o resultado da soma é {resultado}')

def diminuir():
    num1 = float(campo1.get())
    num2 = float(campo2.get())

    resultado = num1 - num2
    total.config(text=f'o resultado da subtração é {resultado}')

def dividir():
    num1 = float(campo1.get())
    num2 = float(campo2.get())

    resultado = num1/num2
    total.config(text=f'o resultado da divisão é {resultado}')

def multiplicar():
    num1 = float(campo1.get())
    num2 = float(campo2.get())

    resultado = num1 * num2
    total.config(text=f'o resultado da multiplicação é {resultado}')

    

# criação da janela
janela = tk.Tk()

#especificar o tamanho da janela definida em pixel
janela.geometry('400x400')

janela.title('Somar')

# caixa de entrada de dados 01
campo1 = tk.Entry (janela)



# exibir na janela
campo1.pack(padx=10, pady=20)


# caixa de entrada de dados 02
campo2 = tk.Entry (janela)

# exibir na janela
campo2.pack(padx=10, pady=10)



#Botão de ação
botao = tk.Button(janela, text='+', command=soma )
botao.pack(pady=10,padx=20, side="left")
botao.place(x=120, y=120)

botao2 = tk.Button(janela, text='-', command=diminuir )
botao2.pack(pady=10,padx=20, side="left")
botao2.place(x=150, y=120)

botao3 = tk.Button(janela, text='/', command=dividir )
botao3.pack(pady=10,padx=20, side="left")
botao3.place(x=180, y=120)

botao4 = tk.Button(janela, text='*', command=multiplicar )
botao4.pack(pady=10,padx=20, side="left")
botao4.place(x=210, y=120)

total = tk.Label(janela, text='total')
total.pack(pady=5)
total.place(x=150, y=150)


# loop principal da interface grafica
janela.mainloop()