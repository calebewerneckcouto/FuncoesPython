'''Escreva uma função que recebe um número inteiro positivo e retorna True caso ele
seja primo e False , caso contrário.
Sugestão:
def e_primo(n):
# Sua implementação aqui
print(e_primo(1))
# False
print(e_primo(2))
# True'''


def primo(n):
    if n <= 1:
        print("Não é primo")
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                print("Não é primo")
                return
        print("É primo")

# Testando
n = int(input("Informe um número para verificação: "))
primo(n)
