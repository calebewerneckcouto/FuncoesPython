```markdown
# Projeto de Funções em Python

Este repositório contém uma coleção de scripts Python cada um demonstrando diferentes algoritmos e funções para operações variadas como cálculo de maior número em uma lista, operações matemáticas como fatorial, verificações de maioridade e presença de elemento em lista, e verificação de número primo.

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

```
/
|-- exercicio.py          # Verificação se um número é primo 
|-- exercicio2.py         # Encontrar o maior número em uma lista 
|-- exercicio3.py         # Verificar maioridade com base na idade 
|-- exercicio4.py         # Verifica maioridade para diferentes tipos de entrada 
|-- exercicio5.py         # Verificar presença de um elemento na lista 
|-- exercicio6.py         # Calcular fatorial de um número
```

## Linguagem de Programação

Este projeto utiliza:
- Python 3

## Dependências e Instalação

Não há dependências externas necessárias para executar estes scripts além de uma versão adequada do Python (Python 3.x). Para instalar Python, visite [python.org](https://www.python.org/downloads/) e siga as instruções para o seu sistema operacional.

## Executando os Scripts e Testes

Para executar qualquer script, abra o terminal e digite, por exemplo:

```bash
python exercicio2.py
```

## Detalhes dos Arquivos de Código

- **`exercicio.py`**:
  - Função `primo(n)`: Verifica se um número inteiro `n` é primo. 
- **`exercicio2.py`**:
  - Função `maior_numero(lista)`: Identifica e retorna o maior número em uma lista e sua posição.
- **`exercicio3.py`**:
  - Função `maior_idade(pessoa)`: Verifica e informa se uma pessoa (tupla com nome e idade) é maior de 18 anos.
- **`exercicio4.py`**:
  - Função `maior_idade(pessoa)`: Verifica e informa, adaptada para tuplas ou dicionários, se uma pessoa é maior de 18 anos.
- **`exercicio5.py`**:
  - Função `elemento_na_lista(lista, elemento)`: Verifica se um elemento está presente em uma lista.
- **`exercicio6.py`**:
  - Função `fatorial(n)`: Calcula o fatorial de um número `n`, com tratamento para valores negativos.

## Exemplos de Uso

Consulte a seção "Exemplos de Uso" em cada descrição de script para visualizar como executar e testar cada função.

## Contribuindo para o Projeto

Para contribuir com melhorias ou correções, siga estes passos:
1. Faça um `fork` do projeto.
2. Crie uma `branch` para sua funcionalidade (`git checkout -b feature/awesomeFeature`).
3. Faça suas alterações.
4. Commit suas mudanças (`git commit -am 'Add some awesomeFeature'`).
5. Realize um `push` para a `branch` criada (`git push origin feature/awesomeFeature`).
6. Abra um `Pull Request`.

## Boas Práticas

- Siga as convenções de nomenclatura e estilo do Python (PEP8).
- Escreva testes unitários para novas funcionalidades.
- Documente as funções adequadamente.
- Certifique-se de que seu código é limpo e bem comentado para manter a legibilidade.
```

### Observação

Esse README foi construído de forma genérica com base na disposição, estrutura e funcionalidades dos scripts fornecidos. Certifique-se de adaptar qualquer parte conforme necessário para refletir mais precisamente os detalhes e nuances do seu projeto específico.