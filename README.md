# README.md

## Projeto: Exercícios de Programação em Python

### Descrição
Este repositório contém uma série de exercícios de programação em Python, cada um focado em diferentes aspectos da linguagem, como estruturas de dados, funções, recursividade e verificação de condições. Os exercícios são úteis para iniciantes e intermediários que desejam praticar e aprimorar suas habilidades em Python.

### Estrutura do Projeto
```
.
├── exercicio4.py
├── exercicio5.py
├── exercicio.py
├── exercicio6.py
├── exercicio2.py
└── exercicio3.py
```

### Linguagens de Programação
- Python

### Dependências e Instruções de Instalação
Este projeto não possui dependências externas. Para rodar os exercícios, você precisará apenas do Python instalado em sua máquina.

**Instruções de Instalação:**
1. Verifique se o Python está instalado em sua máquina:
   ```bash
   python --version
   ```
   ou
   ```bash
   python3 --version
   ```
2. Se o Python não estiver instalado, faça o download e instale a partir do [site oficial](https://www.python.org/downloads/).
3. Clone este repositório ou faça o download dos arquivos `.py`.

### Como Rodar o Projeto e Executar Testes
Para rodar qualquer um dos arquivos, utilize o comando `python` seguido pelo nome do arquivo. Por exemplo:
```bash
python exercicio4.py
```
ou
```bash
python3 exercicio4.py
```

**Execução de Testes:**
Cada arquivo contém testes que são executados ao rodar o script. Não há um framework de testes específico utilizado; os testes são simples chamadas de função com valores conhecidos para verificar a saída.

### Explicação Detalhada dos Arquivos de Código

#### `exercicio4.py`
**Funções:**
- `maior_idade(pessoa)`: Determina se a pessoa é maior de idade.
  - **Argumento**: `pessoa` (tupla ou dicionário)
  - **Funcionamento**:
    - Se `pessoa` é uma tupla, desempacota para obter `nome` e `idade`.
    - Se `pessoa` é um dicionário, usa `get` para obter `nome` e `idade`, com valores padrão se as chaves não estiverem presentes.
    - Imprime se a pessoa é maior ou menor de idade.
  - **Testes**:
    - Tupla: Calebe (36 anos) - Maior de idade.
    - Dicionário: Julia (15 anos) - Menor de idade.
    - Outros casos: Carlos (20 anos) - Maior de idade, Ana (16 anos) - Menor de idade.

#### `exercicio5.py`
**Funções:**
- `elemento_na_lista(lista, elemento)`: Verifica se um elemento está presente em uma lista.
  - **Argumentos**: `lista` (list), `elemento` (qualquer tipo)
  - **Funcionamento**: Itera sobre a lista e compara cada item com o elemento procurado.
  - **Retorno**: `True` se o elemento está na lista, `False` caso contrário.
  - **Testes**:
    - Números: `[1, 2, 3, 4]` contém `3` (True), não contém `5` (False).
    - Strings: `["a", "b", "c"]` contém `"b"` (True), não contém `"d"` (False).

#### `exercicio.py`
**Funções:**
- `primo(n)`: Verifica se um número é primo.
  - **Argumento**: `n` (int)
  - **Funcionamento**:
    - Se `n <= 1`, imprime "Não é primo".
    - Verifica divisores de `2` até `sqrt(n)`.
    - Imprime "É primo" ou "Não é primo" conforme o caso.
  - **Testes**: Solicita um número ao usuário e imprime o resultado.

#### `exercicio6.py`
**Funções:**
- `fatorial(n)`: Calcula o fatorial de um número.
  - **Argumento**: `n` (int)
  - **Condições**:
    - Se `n < 0`, lança `ValueError`.
    - Retorna `1` para `n` igual a `0` ou `1`.
    - **Recursividade**: Retorna `n * fatorial(n - 1)` para `n > 1`.
  - **Testes**: Calcula e imprime o fatorial de `3`, `1`, `0` e `5`.

#### `exercicio2.py`
**Funções:**
- `maior_numero(lista)`: Encontra o maior número em uma lista.
  - **Argumento**: `lista` (list)
  - **Funcionamento**:
    - Retorna `None` se a lista estiver vazia.
    - Percorre a lista para encontrar o maior número e sua posição.
  - **Testes**:
    - `[10, 20, 30, 25]` retorna `(2, 30)`.
    - `[-10, -5, -1, -50]` retorna `(2, -1)`.
    - `[]` retorna `None`.

#### `exercicio3.py`
**Funções:**
- `maior_idade(pessoa)`: Determina se a pessoa é maior de idade.
  - **Argumento**: `pessoa` (tupla)
  - **Funcionamento**: Desempacota a tupla e verifica se a idade é maior ou igual a `18`.
  - **Testes**: 
    - Calebe (36 anos) - Maior de idade.
    - Ana (15 anos) - Menor de idade.

### Exemplos de Uso

#### `exercicio4.py`
```python
maior_idade(("Calebe", 36))  # Saída: Calebe é maior de idade.
maior_idade({"nome": "Julia", "idade": 15})  # Saída: Julia não é maior de idade.
```

#### `exercicio5.py`
```python
print(elemento_na_lista([1, 2, 3, 4], 3))  # Saída: True
print(elemento_na_lista(["a", "b", "c"], "d"))  # Saída: False
```

#### `exercicio.py`
```python
primo(7)  # Saída: É primo
primo(4)  # Saída: Não é primo
```

#### `exercicio6.py`
```python
print(fatorial(5))  # Saída: 120
```

#### `exercicio2.py`
```python
print(maior_numero([10, 20, 30, 25]))  # Saída: (2, 30)
```

#### `exercicio3.py`
```python
maior_idade(("Calebe", 36))  # Saída: Calebe é maior de idade.
maior_idade(("Ana", 15))  # Saída: Ana não é maior de idade.
```

### Boas Práticas e Dicas para Contribuir

1. **Padronização de Nomes**: Mantenha a padronização de nomes de funções e variáveis seguindo o estilo snake_case.
2. **Testes**: Adicione mais casos de testes para cobrir diferentes cenários e garantir a robustez do código.
3. **Refatoração**: Refatore funções que imprimem resultados diretamente para que retornem valores booleanos ou numéricos, facilitando a reutilização em outros contextos.
4. **Documentação**: Adicione docstrings às funções para melhorar a documentação e facilitar o entendimento do código.
5. **Tratamento de Erros**: Implemente tratamento de erros adequado para entradas inválidas.
6. **Contribuições**: Para contribuir, faça um fork do repositório, implemente suas mudanças em uma nova branch e envie um pull request.

### Contribuindo
Para contribuir com este projeto, siga estas etapas:
1. Fork o repositório.
2. Clone o fork para sua máquina local.
3. Crie uma branch para sua funcionalidade ou correção de bug.
4. Faça commit das suas mudanças e push para sua branch.
5. Abra um pull request detalhando suas alterações.

### Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

### Contato
Para dúvidas ou sugestões, entre em contato através de [seu_email@example.com](mailto:seu_email@example.com).

---

**Nota**: Este README.md foi gerado considerando os resumos fornecidos e a estrutura dos arquivos de código. Para mais detalhes, consulte os arquivos diretamente.