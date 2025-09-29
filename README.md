# README.md

## Sobre o Projeto

Este repositório contém vários scripts Python desenvolvidos para exercitar e demonstrar competências básicas em programação Python. Os scripts incluem funções para encontrar o maior número em uma lista, calcular fatoriais, verificar a maioridade, determinar se um número é primo, e verificar a presença de um elemento em uma lista.

### Estrutura de Diretórios

```
/
|-- exercicio.py           # Verifica se um número é primo
|-- exercicio2.py          # Encontra o maior número em uma lista
|-- exercicio3.py          # Avalia maioridade com base em tupla nome-idade
|-- exercicio4.py          # Verifica maioridade usando tupla ou dicionário
|-- exercicio5.py          # Verifica a existência de um elemento em uma lista
|-- exercicio6.py          # Calcula o fatorial de um número
```

### Tecnologias Usadas
- **Python**: Todos os scripts deste repositório são escritos em Python 3.

## Dependências e Instalação

Este projeto não requer a instalação de bibliotecas de terceiros. Para executar qualquer script, você precisa ter o Python 3 instalado em sua máquina. O Python pode ser baixado e instalado a partir de [python.org](https://www.python.org/downloads/).

Para verificar se o Python está instalado, execute:
```sh
python --version
```

## Como Rodar o Projeto

### Execução dos Scripts

Para executar qualquer um dos scripts Python deste repositório, navegue até o diretório contendo o arquivo e execute:

```sh
python nome_do_arquivo.py
```
Substitua `nome_do_arquivo.py` pelo nome do arquivo que deseja executar.

### Executando Testes

Cada arquivo contém blocos de teste no fim do arquivo que podem ser utilizados como exemplos de uso. Para revisar ou alterar os testes, abra o arquivo desejado e modifique as chamadas de funções conforme necessário.

## Detalhamento dos Scripts

1. **exercicio.py**: Implementa uma função `primo(n)` que verifica se um número é primo.
   
2. **exercicio2.py**: Contém a função `maior_numero(lista)`, que retorna a posição e o valor do maior número em uma lista.
   
3. **exercicio3.py**: Define a função `maior_idade(pessoa)` que verifica se uma pessoa (nome, idade) é maior de idade.

4. **exercicio4.py**: Extende `maior_idade(pessoa)` para operar com entradas que podem ser tuplas ou dicionários.

5. **exercicio5.py**: Inclui a função `elemento_na_lista(lista, elemento)` que verifica se um elemento está presente numa lista sem usar o operador `in`.

6. **exercicio6.py**: Fornece a implementação da função `fatorial(n)`, que calcula o fatorial de um número inteiro não-negativo.

## Como Contribuir

Contribuições são sempre bem-vindas! Aqui estão algumas maneiras como você pode contribuir:

- **Propor Melhorias**: Se tiver sugestões para melhorar ou otimizar qualquer script, sinta-se à vontade para propor mudanças.
- **Reportar Bugs**: Encontrou um erro? Abra um issue detalhando o bug e como reproduzi-lo.
- **Adicionar Novas Funcionalidades**: Quer adicionar uma nova funcionalidade? Fork este repositório, faça suas alterações e peça um pull request.

### Boas Práticas de Código

- Mantenha o código limpo e comentado.
- Siga as convenções de nomenclatura padrão de Python (PEP8).
- Escreva testes quando adicionar novas funcionalidades.
- Documente todas as funções públicas com docstrings.

## Licença

Este projeto é distribuído sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes ou visite [MIT License](https://opensource.org/licenses/MIT).