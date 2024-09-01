# Importando a biblioteca tkinter
import tkinter

# Criando um objeto janela
janela = tkinter.Tk()

# Usando o método geometria(está de finindo o tamanho da janela) no OBJ Janela
janela.geometry('500x300')

def clique():
    print('clicou')

texto = tkinter.Label(janela, text="Fazer Login")
texto.pack(padx=10,pady=10)

email = tkinter.Entry(janela, bg='lightblue')
email.pack(padx=10, pady=10)

senha = tkinter.Entry(janela, show="*")
senha.pack(padx=10, pady=10)

checkbox = tkinter.Checkbutton(janela, text="Lembrar Login")
checkbox.pack(padx=10, pady=10)

botao = tkinter.Button(janela, text="login", command=clique, bg='pink')
botao.pack(padx=10, pady=10)

#mantendo a janela aberta
janela.mainloop()
