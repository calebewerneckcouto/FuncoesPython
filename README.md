```markdown
# Projeto de Exerc??cios em Python

Este reposit??rio cont??m uma cole????o de exerc??cios implementados em Python que demonstram diferentes t??cnicas de programa????o, como busca de maior n??mero em uma lista, c??lculo de fatorial, verifica????o de maioridade e determina????o da primalidade de um n??mero.

## Estrutura do Projeto

```
.
????????? exercicio.py          # Verifica se um n??mero ?? primo
????????? exercicio2.py         # Identifica o maior n??mero em uma lista e sua posi????o
????????? exercicio3.py         # Verifica maioridade dado o nome e idade (tupla)
????????? exercicio4.py         # Verifica maioridade com entrada flex??vel (tupla ou dicion??rio)
????????? exercicio5.py         # Verifica a presen??a de um elemento em uma lista
????????? exercicio6.py         # Calcula o fatorial de um n??mero inteiro n??o-negativo
```

## Tecnologias Utilizadas

- Python 3.8+

## Depend??ncias

Este projeto n??o requer depend??ncias externas.

## Instala????o

Clone o reposit??rio usando:

```bash
git clone https://github.com/seuusuario/seuprojeto.git
```

## Executando o Projeto

Cada arquivo pode ser executado individualmente com o comando Python:

```bash
python3 nome_do_arquivo.py
```

## Testes

Cada script possui exemplos de uso que tamb??m servem como testes b??sicos para verificar a funcionalidade. Execute o script correspondente para ver os resultados.

## Detalhes dos Arquivos e Fun????es

1. **exercicio.py**: Cont??m a fun????o `primo(n)` que verifica se um n??mero `n` ?? primo.
   - Entrada: Inteiro positivo
   - Sa??da: Mensagem informando se o n??mero ?? primo.
2. **exercicio2.py**: Inclui a fun????o `maior_numero(lista)` que determina o maior n??mero em uma lista.
   - Entrada: Lista de inteiros
   - Sa??da: Tupla com posi????o e valor do maior n??mero.
3. **exercicio3.py**: Implementa a fun????o `maior_idade(pessoa)` que verifica se uma pessoa (representada por uma tupla) ?? maior de idade.
   - Entrada: Tupla com nome e idade
   - Sa??da: Mensagem sobre a maioridade.
4. **exercicio4.py**: Similar ao `exercicio3.py` mas aceita tanto tupla quanto dicion??rio.
   - Entradas: Tupla ou dicion??rio com nome e idade
   - Sa??da: Mensagem sobre a maioridade dependendo do tipo de entrada.
5. **exercicio5.py**: Desenvolve a fun????o `elemento_na_lista(lista, elemento)` que verifica se um elemento est?? presente em uma lista.
   - Entrada: Lista e um elemento para buscar
   - Sa??da: Booleano indicando presen??a do elemento.
6. **exercicio6.py**: Cont??m a fun????o `fatorial(n)` que calcula o fatorial de um n??mero inteiro n??o-negativo.
   - Entrada: Inteiro n??o-negativo
   - Sa??da: Valor do fatorial.

## Exemplos de Uso

Veja abaixo como voc?? pode usar cada fun????o ap??s a execu????o do script correspondente:

```python
# Verifica????o se n??mero ?? primo
primo(11)

# Encontrar maior n??mero em uma lista
maior_numero([1, 3, 2])

# Verificar maioridade
maior_idade(("Jo??o", 19))

# Verificar maioridade com entrada flex??vel
maior_idade({"nome": "Ana", "idade": 17})

# Verificar presen??a de elemento na lista
elemento_na_lista([1, 2, 3], 2)

# Calcular fatorial
fatorial(5)
```

## Contribuindo

Para contribuir com este projeto, considere as seguintes boas pr??ticas:

1. **Estilo de C??digo**: Siga o guia de estilo PEP 8 para Python.
2. **Documenta????o**: Comente o seu c??digo adequadamente e atualize este README.md se necess??rio.
3. **Testes**: Adicione exemplos ou testes para novas funcionalidades.
4. **Revis??o**: Fa??a pull requests para revis??o de c??digo e teste antes de incorporar novas mudan??as.

### Dicas para contribuir

- Explore os scripts existentes para entender as funcionalidades presentes.
- Verifique issues abertos para encontrar ??reas que requerem melhorias ou novas funcionalidades.

```

Este README fornece uma vis??o geral do projeto, facilitando a compreens??o e contribui????o para o mesmo por parte de outros desenvolvedores.