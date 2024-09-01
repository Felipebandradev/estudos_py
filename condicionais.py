# Autenticação com usuário e senha

login = input("Digite seu usuário: ")
senha = input("Digite sua senha: ")

# Declarando as condicionais

if login == 'user' and senha == '123' or login == 'admim' and senha == "456":
    print("Login ok")
    
    # Para condicionais encadeadas o código PRECISA SER BEM IDENTADO ou Seja ORGANIZADO
    chave = input("Digite a chave de segurança: ")
    
    if chave == "bolinho":
        print("Chave ok")
        
    else: 
        print("Chave invalida")
    
    
else :
    print("Login inválido")