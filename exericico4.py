'''Adapte a função maior_idade(pessoa) de forma que ela possa receber tanto uma
tupla quanto um dicionário. Dica: método type pode te ajudar.
'''


def maior_idade(pessoa):
    if isinstance(pessoa, tuple):  # Verifica se a entrada é uma tupla
        nome, idade = pessoa
    elif isinstance(pessoa, dict):  # Verifica se a entrada é um dicionário
        nome = pessoa.get("nome", "Pessoa")  # Pega o nome, ou "Pessoa" como padrão
        idade = pessoa.get("idade", 0)  # Pega a idade, ou 0 como padrão
    else:
        print("Formato inválido!")
        return

    if idade >= 18:
        print(f"{nome} é maior de idade.")
    else:
        print(f"{nome} não é maior de idade.")

# Testando a função com tuplas e dicionários
maior_idade(("Calebe", 36))  # Calebe é maior de idade.
maior_idade({"nome": "Julia", "idade": 15})  # Julia não é maior de idade.
maior_idade({"nome": "Carlos", "idade": 20})  # Carlos é maior de idade.
maior_idade(("Ana", 16))  # Ana não é maior de idade.
