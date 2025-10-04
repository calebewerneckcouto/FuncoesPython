```markdown
# Python Utility Functions

# 🎬 Sistema de Geração de Vídeos com IA

[![Demonstração do Sistema](https://img.youtube.com/vi/ABCD123456/0.jpg)]([https://www.youtube.com/watch?v=ABCD123456](https://www.youtube.com/watch?v=20E3Wfdfbzk&list=RD20E3Wfdfbzk&start_radio=1))

*Clique na imagem acima para ver a demonstração completa do sistema*

Este repositório contém uma coleção de funções utilitárias em Python, que incluem operações como encontrar o maior número em uma lista, calcular o fatorial de um número, verificar a maioridade de uma pessoa, determinar se um número é primo, e verificar a presença de um elemento em uma lista sem usar o operador `in`.

## Estrutura do Projeto

O projeto está organizado em arquivos Python individuais, cada um contendo funções específicas para realizar tarefas particulares:

```
/
│
├── exercicio.py        # Função para verificar se um número é primo
├── exercicio2.py       # Função para encontrar o maior número e sua posição em uma lista
├── exercicio3.py       # Função para verificar a maioridade de uma pessoa (baseado em tuplas)
├── exercicio4.py       # Função para verificar a maioridade de uma pessoa (baseado em diferentes estruturas de dados)
├── exercicio5.py       # Função para verificar a presença de um elemento em uma lista sem usar `in`
└── exercicio6.py       # Função para calcular o fatorial de um número
```

## Linguagem de Programação Utilizada

- Python 3

## Dependências e Instruções de Instalação

Este projeto não depende de nenhuma biblioteca externa além da biblioteca padrão do Python. Para executar qualquer um dos scripts, você precisará ter Python 3 instalado em seu sistema. Você pode baixar e instalar o Python através do seguinte link:

- [Download Python](https://www.python.org/downloads/)

Após a instalação do Python, você pode executar qualquer script diretamente do terminal. Por exemplo:

```bash
python exercicio2.py
```

## Como rodar o projeto e executar testes

Cada arquivo é independente e contém funções específicas com blocos de teste no final do arquivo (quando aplicável). Para executar qualquer um dos arquivos e ver os resultados dos testes:

```bash
python nome_do_arquivo.py
```

## Principais Responsabilidades dos Arquivos

### `exercicio.py`

- **Função `primo(n)`**:
  - **Responsabilidade**: Verificar se um número inteiro é primo.
  - **Comportamento**: Imprime se o número é primo ou não baseado em uma checagem de divisores.

### `exercicio2.py`

- **Função `maior_numero(lista)`**:
  - **Responsabilidade**: Identificar o maior número em uma lista e sua posição.
  - **Comportamento**: Retorna uma tupla com a posição e o valor do maior número.

### `exercicio3.py` e `exercicio4.py`

- **Função `maior_idade(pessoa)`**:
  - **Responsabilidade**: Avaliar se a pessoa é maior de idade.
  - **Comportamento**: Imprime se a pessoa é maior de idade baseado em sua idade, tratando diferentes estruturas de dados.

### `exercicio5.py`

- **Função `elemento_na_lista(lista, elemento)`**:
  - **Responsabilidade**: Verificar a presença de um elemento em uma lista manualmente.
  - **Comportamento**: Retorna `True` se o elemento está presente na lista, caso contrário `False`.

### `exercicio6.py`

- **Função `fatorial(n)`**:
  - **Responsabilidade**: Calcular o fatorial de um número.
  - **Comportamento**: Retorna o valor fatorial de um número inteiro não-negativo.

## Exemplos de Uso

Você pode encontrar exemplos específicos de uso dentro de cada arquivo, testando as respectivas funções.

## Boas Práticas e Dicas para Contribuir

- **Siga o PEP8** para estilo de codificação Python.
- **Escreva testes** para novas funcionalidades.
- **Documente novas funções** com docstrings.
- **Use nomes descritivos** para variáveis e funções.
- Antes de submeter uma nova funcionalidade, **revise o código** para garantir que esteja limpo e organizado.

Contribuições são sempre bem-vindas! Clone o repositório, faça as suas alterações e submeta um pull request.
```
Este README fornece uma visão geral abrangente do projeto, incluindo instruções sobre como instalá-lo, usá-lo e contribuir para ele.
