```markdown
# README.md - Repositório de Exercícios Python

Este repositório contém uma coleção de exercícios implementados em Python, cada um focado em conceitos específicos de programação, como recursão, controle de fluxo, tratamento de exceções e manipulação de dados.

## Estrutura do Projeto e Pastas

O projeto é organizado nas seguintes pastas:
- `src` - Contém os scripts Python com os exercícios implementados.
- `tests` - Contém os testes unitários para os exercícios (quando aplicável).

Arquivos específicos:
- `exercicio.py`: Verifica se um número é primo.
- `exercicio2.py`: Encontra o maior número numa lista e sua posição.
- `exercicio3.py`: Verifica se uma pessoa é maior de idade.
- `exercicio4.py`: Flexível verificação de maioridade, aceitando diferentes estruturas de dados.
- `exercicio5.py`: Verifica a presença de um elemento em uma lista sem usar o operador `in`.
- `exercicio6.py`: Calcula o fatorial de um número usando recursão.

## Linguagens de Programação Usadas

- **Python**: Versão 3.8 ou superior.

## Dependências e Instruções de Instalação

Para rodar os scripts e testes, é recomendado ter o Python 3.8 ou superior instalado. Não há dependências externas necessárias para a execução dos exercícios contidos neste repositório.

Instalação do Python:
```bash
sudo apt update
sudo apt install python3.8
```

## Como Rodar o Projeto e Executar Testes

Navegue até a pasta do projeto e execute os scripts Python diretamente com o comando:
```bash
python3 nome_do_arquivo.py
```

Para rodar testes (quando aplicável):
```bash
python3 -m unittest tests/nome_do_arquivo_de_teste.py
```

## Explicação Detalhada dos Arquivos de Código

### `exercicio.py`
- **Função `primo(n)`**: Verifica se o número `n` é primo, imprimindo o resultado diretamente.

### `exercicio2.py`
- **Função `maior_numero(lista)`**: Encontra o maior número em uma lista e retorna sua posição e valor.

### `exercicio3.py` e `exercicio4.py`
- Ambos verificam a maioridade de uma pessoa, mas `exercicio4.py` aceita tanto tuplas quanto dicionários como entrada.

### `exercicio5.py`
- **Função `elemento_na_lista(lista, elemento)`**: Verifica se um elemento está presente na lista, através de uma iteração explícita.

### `exercicio6.py`
- **Função `fatorial(n)`**: Calcula o fatorial de `n` recursivamente, tratando de casos especiais e exceções.

## Exemplos de Uso

### Uso de `exercicio2.py`
```python
result = maior_numero([10, 20, 30, 25])
print(result)  # Saída: (2, 30)
```

## Boas Práticas e Dicas para Contribuir

- **Estilo de Código**: Siga o guia de estilo PEP8 para Python.
- **Testes**: Garanta que há testes cobrindo novas funcionalidades ou corrigindo bugs.
- **Documentação**: Documente funções e métodos claramente.
- **Pull Requests**: Envie PRs pequenos e focados, um para cada funcionalidade ou correção.

## Como Contribuir

1. Clone o repositório.
2. Crie uma branch para sua funcionalidade ou correção de bugs.
3. Faça suas alterações.
4. Execute os testes.
5. Envie um pull request.

**Obrigado por contribuir!**
```