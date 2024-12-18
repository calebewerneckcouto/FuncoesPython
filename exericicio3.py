''' Implemente uma função maior_idade(pessoa) que receba uma tupla representando
uma pessoa com nome e idade e imprime na tela se a pessoa é maior de idade ou
não.
'''


def maior_idade(pessoa):
    nome, idade = pessoa 
    if idade >= 18:
        print(f"{nome} é maior de idade.")
    else:
        print(f"{nome} não é maior de idade.")


maior_idade(("Calebe", 36))  
maior_idade(("Julia", 15))  
