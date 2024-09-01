# Criando um lista não ordenada
lista = [5, 7,6,3,9,4,8]

# Resgatando o primeiro elemento da lista
print(lista[0])

# Exibindo a lista 
print(lista)

# Retornando o tamanho de uma lista
n = len(lista)

for i in range(n - 1):
    for i in range(n - 1):
        # comparando os itens
        if lista[i] > lista[i+1]:
            #trocando de posição os elementos da lista
            lista[i], lista[i+1] = lista[i+1], lista[i]

print(lista)