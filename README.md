# README.md

## Overview
Este repositório contém uma coleção de exercícios em Python destinados à prática de habilidades de programação, focando em operações com listas, recursividade, condições e loops. Cada arquivo de script Python encapsula uma funcionalidade específica detalhada abaixo.

## Estrutura do Projeto
O repositório está organizado da seguinte forma:

```
/projeto
    /exercicio2.py     # Encontrar o maior número em uma lista e seu índice
    /exercicio3.py     # Avaliar se uma pessoa (nome, idade) é maior de idade
    /exercicio4.py     # Tratar diferentes estruturas para verificar maioridade
    /exercicio5.py     # Determinar se um elemento está presente em uma lista
    /exercicio6.py     # Calcular o fatorial de um número
    /exercicio.py      # Verificar se um número é primo
```

## Linguagens de Programação Utilizadas
- Python 3.x

## Dependências e Instruções de Instalação
Não há dependências externas requeridas para executar estes scripts, pois eles usam apenas a biblioteca padrão de Python. Para executar qualquer um dos scripts, é necessário ter Python 3.x instalado localmente.

Para instalar Python, você pode baixar o instalador apropriado para seu sistema operacional em [python.org](https://www.python.org/downloads/).

## Como Rodar o Projeto e Executar Testes 
Para executar qualquer script, utilize o seguinte comando no terminal (substitua `<nome_do_script>.py` pelo nome do arquivo que deseja executar):

```bash
python <nome_do_script>.py
```

Para rodar um teste específico dentro do arquivo, certifique-se de invocar a função de teste nesse arquivo ou adicionar um bloco de teste ao final do arquivo. Por exemplo:

```python
if __name__ == "__main__":
    print(maior_numero([10, 20, 30, 25]))
```

## Descrição dos Scripts
- **exercicio2.py**: Contém a função `maior_numero`, que identifica o maior número em uma lista de números inteiros, retornando a posição e o número.
- **exercicio3.py** e **exercicio4.py**: Ambos lidam com a avaliação da maioridade de uma pessoa, mas `exercicio4.py` acrescenta suporte para entrada de dados tanto em formato de tupla quanto de dicionário.
- **exercicio5.py**: Implementa a função `elemento_na_lista`, que verifica se um elemento está contido em uma lista fornecida.
- **exercicio6.py**: Contém a função `fatorial`, que calcula o fatorial de um número inteiro não-negativo de maneira recursiva.
- **exercicio.py**: Fornece a função `primo`, que determina se um número é primo.

## Exemplos de Uso

```python
# exemplo de uso para o exercicio2.py
print(maior_numero([10, 20, 30, 25]))  # Saída: (2, 30)

# exemplo de uso para o exercicio5.py
print(elemento_na_lista([1, 2, 3, 4], 3))  # Saída: True
```

## Como Contribuir
- Estude os scripts existentes e entenda suas funcionalidades.
- Mantenha a simplicidade e siga as convenções de código Python PEP 8.
- Escreva comentários claros e funções bem documentadas.
- Para contribuir com código, considere fazer um fork do repositório, realizar suas mudanças e submeter um Pull Request.

Agradecemos sua contribuição para tornar este projeto ainda melhor!