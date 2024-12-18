'''Implemente uma função que recebe uma lista de números inteiros e retorna uma
tupla (pos, num) , onde pos é a posição (ou índice) do maior número na lista e num
é o valor desse número.
'''


def maior_numero(lista):
    if not lista:  
        return None  
    pos = 0
    num = lista[0]
    for i in range(1, len(lista)):
        if lista[i] > num:
            num = lista[i]
            pos = i
    return (pos, num)


print(maior_numero([10, 20, 30, 25]))  # (2, 30)
print(maior_numero([-10, -5, -1, -50]))  # (2, -1)
print(maior_numero([]))  # None
