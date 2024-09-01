# Importando a biblioteca tkinter
import tkinter

# Criando o objeto janela
janela = tkinter.Tk()

janela.geometry('600x600')

def clique():
    print('cadastrou')

texto = tkinter.Label(janela, text="Fazer Cadastro")
texto.pack(padx=10,pady=10)

textoNome = tkinter.Label(janela, text="Nome")
textoNome.pack(padx=10,pady=10)

nomemail = tkinter.Entry(janela)
nomemail.pack(padx=10,pady=10)


textoEmail = tkinter.Label(janela, text="E-mail")
textoEmail.pack(padx=10,pady=10)

email = tkinter.Entry(janela)
email.pack(padx=10,pady=10)

textoNascimento = tkinter.Label(janela, text="Nascimento")
textoNascimento.pack(padx=10,pady=10)

nascimento = tkinter.Entry(janela)
nascimento.pack(padx=10,pady=10)

botao = tkinter.Button(janela, text="login", command=clique, bg='green', width='50', fg='white')
botao.pack(padx=10, pady=10)




janela.mainloop()
