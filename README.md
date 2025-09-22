# README.md for Python Examples Repository

## Descrição do Projeto

Este repositório contém uma coleção de programas Python simples, cada um ilustrando um conceito específico ou técnica de programação. Estes exemplos são ideais para novos programadores que estão aprendendo os básicos de Python ou programadores mais experientes que precisam relembrar certos conceitos.

## Estrutura do Projeto

O projeto inclui os seguintes arquivos Python distribuídos na raiz do repositório:

- `exercicio.py`: Programa que determina se um dado número inteiro é primo.
- `exercicio2.py`: Programa que identifica o maior número em uma lista e retorna a sua posição.
- `exercicio3.py`: Programa que verifica se uma pessoa é maior de idade a partir de uma tupla com nome e idade.
- `exercicio4.py`: Programa similar ao `exercicio3.py`, com suporte adicional para entrada como dicionário.
- `exercicio5.py`: Programa que verifica se um elemento específico está presente em uma lista sem usar o operador `in`.
- `exercicio6.py`: Programa que calcula o fatorial de um número usando recursão.

## Linguagens de Programação

- Python 3.x

## Dependências

Este projeto não requer nenhuma biblioteca externa além do Python 3.x que deve estar instalado no seu sistema.

### Instalação do Python

- **Windows/Mac/Linux**: Visite [python.org](https://www.python.org/downloads/) para baixar e instalar o interpretador Python apropriado para seu sistema operacional.

## Como Utilizar

Cada script pode ser executado de forma independente. Abaixo estão as instruções para executar os programas em um terminal.

```bash
python exercicio.py    # Para verificar se um número é primo
python exercicio2.py   # Para identificar o maior número em uma lista
python exercicio3.py   # Para verificar maioridade com base em uma tupla
python exercicio4.py   # Para verificar maioridade com suporte a tupla ou dicionário
python exercicio5.py   # Para verificar a presença de um elemento em uma lista
python exercicio6.py   # Para calcular o fatorial de um número
```

## Execução de Testes

Cada arquivo inclui exemplos internos ou um bloco específico para testar a funcionalidade implementada. Esses exemplos são tipicamente localizados ao final de cada arquivo.

## Contribuindo

Se você deseja contribuir para este projeto, por favor siga as seguintes boas práticas:

- **Use Pull Requests**: Faça alterações em uma branch separada e solicite merges via pull requests.
- **Padronização de Código**: Siga o guia de estilo [PEP 8](https://pep8.org/).
- **Documentação**: Comente seu código adequadamente e atualize este README.md se necessário.
- **Testes**: Certifique-se de incluir testes para novas funcionalidades e executá-los antes de solicitar a inclusão ao projeto principal.

## Exemplos de Uso

1. **Determinar se um número é primo**
   ```python
   primo(17)  # Deve imprimir "É primo"
   primo(4)   # Deve imprimir "Não é primo"
   ```

2. **Identificar o maior número em uma lista**
   ```python
   maior_numero([1, 3, 5, 7, 9])  # Retorna (4, 9)
   ```

3. **Verificar a maioridade de uma pessoa**
   ```python
   maior_idade(("Gabriel", 21))  # Imprime "Gabriel é maior de idade."
   maior_idade({"nome": "Ana", "idade": 16})  # Imprime "Ana não é maior de idade."
   ```

Esperamos que este repositório seja útil para a sua aprendizagem ou revisão de conceitos de programação em Python. Boa programação!
