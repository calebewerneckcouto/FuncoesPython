```markdown
# Projeto de Funções em Python

Este repositório contém uma coleção de scripts Python, cada um implementando uma funcionalidade específica. As funções abrangem operações matemáticas simples, validações de dados e métodos de busca em listas.

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

- `exercicio2.py`: Encontra o maior número em uma lista e sua posição.
- `exercicio3.py`: Verifica se uma pessoa é maior de idade.
- `exercicio4.py`: Verifica maior de idade considerando entradas em diferentes formatos.
- `exercicio5.py`: Busca de um elemento em uma lista sem usar o operador `in`.
- `exercicio6.py`: Calcula o fatorial de um número inteiro não-negativo.
- `exercicio.py`: Avalia se um número é primo.

## Linguagens de Programação Usadas

- **Python**: Versão 3.x

## Dependências e Instruções de Instalação

Este projeto não requer nenhuma dependência externa além do Python 3.x. Para instalar o Python, siga as instruções de instalação disponíveis em [python.org](https://www.python.org/downloads/).

## Como Rodar o Projeto e Executar Testes

Para executar qualquer script, utilize o comando abaixo no terminal:

```bash
python <nome_do_arquivo>.py
```

## Detalhamento dos Arquivos de Código

### `exercicio2.py`

#### Funções:

- `maior_numero(lista)`: Identifica o maior número em uma lista e sua posição. Retorna uma tupla `(posição, número)` ou `None` para listas vazias.

### `exercicio3.py`

#### Funções:

- `maior_idade(pessoa)`: Verifica se uma pessoa (dada como uma tupla nome-idade) é maior de idade.

### `exercicio4.py`

#### Funções:

- `maior_idade(pessoa)`: Avalia a maioridade com base em dados de entrada que podem ser tuplas ou dicionários.

### `exercicio5.py`

#### Funções:

- `elemento_na_lista(lista, elemento)`: Verifica a existência de um elemento em uma lista sem usar o operador `in`.

### `exercicio6.py`

#### Funções:

- `fatorial(n)`: Calcula o fatorial de um número inteiro `n`. Retorna `1` para `0` ou `1` e utiliza recursão para outros valores.

### `exercicio.py`

#### Funções:

- `primo(n)`: Determina se um número `n` é primo. Imprime diretamente no console.

## Exemplos de Uso

Cada arquivo contém exemplos de uso como parte de seu código, demonstrando as chamadas às funções implementadas.

## Boas Práticas e Dicas para Contribuir

1. **Leia o código existente**: Familiarize-se com o projeto e seu estilo de codificação.
2. **Documente suas mudanças**: Sempre comente seu código quando adicionar ou alterar funcionalidades.
3. **Use nomes explicativos**: Variáveis e funções devem ter nomes que refletem seu propósito.
4. **Escreva testes**: Adicione testes para novas funcionalidades para garantir estabilidade.
5. **Revisão de código**: Solicite revisões de código para garantir qualidade e colaboração.

## Licença

Este projeto é distribuído sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
```