# README.md

## Projeto de Funções em Python

Este repositório contém uma série de exercícios de Python implementando diferentes funcionalidades, desde a determinação se um número é primo até a identificação da maioridade de uma pessoa. Cada script é independente e implementa uma função específica juntamente com alguns testes para mostrar sua execução e resultados esperados.

### Estrutura do Projeto

O repositório é organizado da seguinte forma:

- **exercicio.py**: Verifica se um número inteiro é primo.
- **exercicio2.py**: Encontra o maior número em uma lista e sua posição.
- **exercicio3.py**: Determina se uma pessoa (dada por nome e idade) é maior de idade.
- **exercicio4.py**: Similar ao `exercicio3.py`, mas adapta para entrada de dados como tuplas ou dicionários.
- **exercicio5.py**: Verifica a presença de um elemento em uma lista.
- **exercicio6.py**: Calcula o fatorial de um número.

### Linguagens de Programação Utilizadas

- **Python 3.8+** é a linguagem usada em todo o projeto.

### Dependências e Instruções de Instalação

Não há dependências externas necessárias para rodar os scripts deste repositório, uma vez que todos usam a biblioteca padrão de Python. Para executá-los, você só precisa ter o Python instalado em seu ambiente. Você pode baixar e instalar o Python [aqui](https://www.python.org/downloads/).

### Como Rodar o Projeto e Executar Testes

Para executar qualquer script, navegue até o diretório do projeto em seu terminal e execute:

```sh
python3 <nome_do_arquivo.py>
```

Substitua `<nome_do_arquivo.py>` pelo nome do script que deseja rodar. Cada arquivo já contém exemplos de teste no seu bloco main que ilustram como as funções devem ser usadas e os resultados esperados.

### Descrição Detalhada dos Arquivos de Código

Aqui segue uma breve descrição de cada arquivo junto com suas funções e responsabilidades principais:

1. **exercicio.py**: Implementa a função `primo(n)` que verifica se 'n' é um número primo.
    - **Testes**: Permite ao usuário inserir um número para verificar sua primalidade.
    
2. **exercicio2.py**: Contém a função `maior_numero(lista)` para encontrar o maior número em uma lista e sua posição.
    - **Exemplos de Uso**: Vários casos de testes são fornecidos para listas com valores distintos e também para uma lista vazia.

3. **exercicio3.py** e **exercicio4.py**: Ambos tratam de verificar se uma pessoa é maior de idade, mas o `exercicio4.py` aceita entrada como tupla ou dicionário.
    - **Flexibilidade**: `exercicio4.py` demonstra uma maior adaptabilidade em relação ao formato dos dados de entrada.
    
4. **exercicio5.py**: Define a função `elemento_na_lista(lista, elemento)` para pesquisar manualmente (sem usar o operador `in`) se um elemento está presente na lista.

5. **exercicio6.py**: Calcula o fatorial de um número inteiro com a função `fatorial(n)`, com tratamentos de erros básicos.
    - **Recursividade**: Demonstra o uso de chamadas recursivas para resolver um problema matemático.

### Exemplos de Uso

Por favor, consulte a seção "Como Rodar o Projeto e Executar Testes" para ver como você pode executar cada script e ver demonstrações de seu funcionamento.

### Boas Práticas e Dicas para Contribuir

- **Estilo de Código**: Siga a [PEP 8](https://pep8.org/), a guia de estilo para Python.
- **Documentação**: Comente seu código adequadamente e atualize este README se adicionando novas funcionalidades.
- **Testes**: Adicione exemplos de testes quando contribuir com novas funções.
- **Pull Requests**: Use pull requests para revisão de código antes de mergear novas funcionalidades na branch principal.

Para contribuir, faça um fork do repositório, crie uma nova branch para suas funcionalidades ou correções, faça commits de suas mudanças, e então crie um pull request para revisão.