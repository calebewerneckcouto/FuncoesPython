# Projeto de Fun????es Utilit??rias em Python

Este reposit??rio cont??m uma cole????o de exerc??cios implementados em Python, consistindo em fun????es ??teis e pr??ticas para realizar tarefas como encontrar o maior n??mero em uma lista, calcular o fatorial de um n??mero, verificar a maioridade e determinar se um n??mero ?? primo.

## Estrutura do Projeto

O projeto est?? organizado da seguinte forma:

- `exercicio.py`: Cont??m uma fun????o que verifica se um n??mero ?? primo.
- `exercicio2.py`: Implementa uma fun????o que retorna a posi????o e o valor do maior n??mero em uma lista.
- `exercicio3.py`: Define uma fun????o que verifica se uma pessoa ?? maior de idade usando tuplas.
- `exercicio4.py`: Implementa uma fun????o que verifica a maioridade usando tanto tuplas quanto dicion??rios.
- `exercicio5.py`: Cont??m uma fun????o para verificar a presen??a de um elemento em uma lista.
- `exercicio6.py`: Fornece uma fun????o que calcula o fatorial de um n??mero de forma recursiva.

## Tecnologias Utilizadas

- **Linguagem de Programa????o**: Python 3

## Depend??ncias

Este projeto n??o requer depend??ncias externas, apenas o Python 3 instalado na sua m??quina. Para instalar o Python, voc?? pode seguir as instru????es no [site oficial do Python](https://www.python.org/downloads/).

## Como Executar o Projeto

Cada arquivo Python pode ser executado de forma independente atrav??s da linha de comando. Por exemplo, para executar o arquivo `exercicio2.py`, voc?? pode usar:

```bash
python3 exercicio2.py
```

### Como Executar Testes

Cada script cont??m exemplos de uso ou testes no final do arquivo. Para rodar os testes, execute o script desejado no terminal. Isso mostrar?? os resultados dos testes direto no console.

## Detalhamento dos Arquivos de C??digo

### `exercicio.py`

- **Fun????o `primo(n)`**: Verifica se um n??mero ?? primo. Espera-se que o usu??rio insira um n??mero e a fun????o determinar?? se ?? primo ou n??o, imprimindo o resultado na sa??da padr??o.

### `exercicio2.py`

- **Fun????o `maior_numero(lista)`**: Retorna a posi????o e o valor do maior n??mero em uma lista fornecida. Se a lista estiver vazia, retorna `None`.

### `exercicio3.py`

- **Fun????o `maior_idade(pessoa)`**: Avalia se uma pessoa (representada por uma tupla contendo nome e idade) ?? maior de idade. Imprime uma mensagem indicando a maioridade.

### `exercicio4.py`

- **Fun????o `maior_idade(pessoa)`**: Similar ?? fun????o em `exercicio3.py` mas aceita tanto tuplas quanto dicion??rios para representar a pessoa.

### `exercicio5.py`

- **Fun????o `elemento_na_lista(lista, elemento)`**: Verifica a presen??a de um elemento em uma lista dada. Retorna `True` se o elemento estiver presente, caso contr??rio `False`.

### `exercicio6.py`

- **Fun????o `fatorial(n)`**: Calcula o fatorial de um n??mero usando a t??cnica de recursividade. Se o n??mero fornecido for negativo, gera um `ValueError`.

## Exemplos de Uso

Voc?? pode testar cada script individualmente executando-os no terminal. Por exemplo, para verificar a funcionalidade do fatorial:

```bash
python3 exercicio6.py
```

E siga as instru????es fornecidas pelo script, se houver.

## Como Contribuir

Para contribuir com este reposit??rio, voc?? pode seguir as boas pr??ticas abaixo:

1. **Use Branches**: N??o fa??a commit diretamente na branch principal. Crie uma branch para cada nova caracter??stica ou corre????o.
2. **C??digo Limpo e Comentado**: Escreva um c??digo limpo e bem comentado para que outros desenvolvedores possam entender facilmente.
3. **Pull Requests**: Envie pull requests com uma descri????o clara das mudan??as propostas e suas justificativas.
4. **Revis??o de C??digo**: Solicite revis??es de c??digo para garantir qualidade e corretude.
5. **Testes**: Adicione testes sempre que poss??vel, para garantir que as fun????es estejam operando como esperado.

Contribui????es s??o sempre bem-vindas para melhorar as funcionalidades ou corrigir bugs!