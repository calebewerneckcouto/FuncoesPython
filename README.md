# Projeto de Funções Python

Este repositório contém uma coleção de scripts Python, cada um implementando uma funcionalidade específica, como identificação do maior número em uma lista, cálculo de fatorial, verificação de maioridade, determinação da primalidade de um número e verificação da presença de um elemento em uma lista. Abaixo estão detalhadas as informações referentes à estrutura do projeto, uso e contribuições.

## Estrutura do Projeto

O projeto está organizado nas seguintes pastas e arquivos principais:

```
/projeto-funcoes-python
│
├── exercicio.py                # Verificação se um número é primo
├── exercicio2.py               # Identifica maior número em uma lista
├── exercicio3.py               # Verificação de maioridade
├── exercicio4.py               # Versão avançada da verificação de maioridade para diferentes tipos de input
├── exercicio5.py               # Verificação de presença de elemento em lista
└── exercicio6.py               # Cálculo de fatorial de um número
```

## Linguagens Utilizadas

- Python 3

## Dependências e Instruções de Instalação

Este projeto não requer a instalação de bibliotecas externas, pois utiliza apenas recursos da linguagem Python padrão. Para executar os scripts, você precisa ter Python 3 instalado em seu ambiente. Se necessário, você pode instalar o Python através do seguinte site: [python.org](https://www.python.org/downloads/).

## Como rodar o projeto e executar testes

Para executar qualquer script individualmente, use o seguinte comando na linha de terminal, enquanto estiver no diretório do projeto:

```bash
python <nome_do_arquivo>.py
```
Para cada arquivo, são previstos testes embutidos que demonstrarão a funcionalidade implementada.

## Descrição Detalhada dos Arquivos de Código

A seguir, uma explicação das principais funções presentes em cada arquivo:

1. **exercicio.py**:
    - `primo(n)`: verifica se o número `n` é primo.

2. **exercicio2.py**:
    - `maior_numero(lista)`: retorna a posição e o valor do maior número numa lista.

3. **exercicio3.py**:
    - `maior_idade(pessoa)`: verifica se uma pessoa (nome, idade) é maior de idade.

4. **exercicio4.py**:
    - `maior_idade(pessoa)`: versão avançada que suporta input tanto em formato de tupla quanto de dicionário.

5. **exercicio5.py**:
    - `elemento_na_lista(lista, elemento)`: verifica a presença de um elemento específico numa lista.

6. **exercicio6.py**:
    - `fatorial(n)`: calcula o fatorial de um número `n`.

## Exemplos de Uso

Para verificar se um número é primo:

```python
# arquivo: exercicio.py
primo(29) # Output: "É primo"
```

Para encontrar o maior número em uma lista:

```python
# arquivo: exercicio2.py
maior_numero([1, 3, 5, 7, 9]) # Output: (4, 9)
```

## Boas Práticas e Dicas para Contribuir

- **Clonando o Repositório**: Inicie fazendo um fork e, em seguida, clone o repositório para fazer as suas alterações.
- **Documentação**: Mantenha os comentários atualizados e claros.
- **Testes**: Adicione testes para novas funcionalidades garantindo que não quebrarão funcionalidades existentes.
- **Codificação**: Siga as convenções de codificação do Python (PEP 8).
- **Pull Requests**: Faça pull requests pequenos, que solucionem apenas um problema por vez.

Para contribuições, por favor, crie uma issue explicando a alteração proposta ou o bug a ser corrigido. Em seguida, faça um fork do projeto, realize as alterações em uma branch separada e submeta um pull request.