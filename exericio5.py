'''Implemente uma função que recebe dois argumentos, uma lista e um elemento , e
retorna True caso elemento seja encontrado na lista , e False caso contrário. Não
é permitido utilizar o método in .'''

def elemento_na_lista(lista, elemento):
    for i in range(len(lista)):  # Itera sobre os índices da lista
        if lista[i] == elemento:  # Compara o elemento atual com o procurado
            return True  # Retorna True se encontrar o elemento
    return False  # Retorna False se não encontrar o elemento após percorrer a lista

# Testando a função
print(elemento_na_lista([1, 2, 3, 4], 3))  # True
print(elemento_na_lista([1, 2, 3, 4], 5))  # False
print(elemento_na_lista(["a", "b", "c"], "b"))  # True
print(elemento_na_lista(["a", "b", "c"], "d"))  # False

