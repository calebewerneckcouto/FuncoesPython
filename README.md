# README.md

## Projeto: Exercícios de Programação em Python

Este repositório contém uma coleção de exercícios de programação em Python, cada um focando em diferentes aspectos da linguagem e problemas algorítmicos. Os exercícios são projetos simples que podem ser úteis para iniciantes e para quem deseja aprimorar suas habilidades em Python.

### Estrutura do Projeto

```
.
├── exercicio2.py
├── exercicio6.py
├── exericicio3.py
├── exericico4.py
└── exericio5.py
```

### Linguagens de Programação

- **Python**: Todos os arquivos são escritos em Python 3.

### Dependências

- Não há dependências externas para este projeto. Apenas a instalação do Python 3 é necessária.

### Instruções de Instalação

1. **Instalar Python**: Certifique-se de ter o Python 3 instalado em sua máquina. Você pode baixá-lo a partir do [site oficial](https://www.python.org/downloads/).

2. **Clonar o Repositório**: Clone este repositório usando o comando abaixo:

   ```bash
   git clone https://github.com/seuusuario/seuprojeto.git
   ```

3. **Navegar até o Diretório do Projeto**:

   ```bash
   cd seuprojeto
   ```

### Como Rodar o Projeto

Para rodar qualquer um dos arquivos, utilize o interpretador Python no terminal:

```bash
python nome_do_arquivo.py
```

### Como Executar Testes

Os testes estão incluídos dentro de cada arquivo. Basta rodar o arquivo para que os testes sejam executados automaticamente.

### Explicação Detalhada dos Arquivos de Código

#### `exercicio2.py`

**Função `maior_numero`:**

- **Parâmetro**: Uma lista de números inteiros.
- **Retorno**: Uma tupla `(pos, num)` onde `pos` é a posição do maior número na lista e `num` é o valor desse número.
- **Responsabilidades**:
  - Verifica se a lista está vazia e retorna `None` caso esteja.
  - Assume inicialmente que o primeiro elemento é o maior.
  - Percorre a lista para encontrar o maior número e sua posição.
- **Testes**:
  - `[10, 20, 30, 25]` -> Retorna `(2, 30)`
  - `[-10, -5, -1, -50]` -> Retorna `(2, -1)`
  - `[]` -> Retorna `None`

#### `exercicio6.py`

**Função `fatorial`:**

- **Parâmetro**: Um número inteiro não-negativo `n`.
- **Responsabilidades**:
  - Lança `ValueError` se `n` for negativo.
  - Retorna 1 se `n` for 0 ou 1.
  - Calcula o fatorial de `n` usando recursividade.
- **Testes**:
  - `fatorial(3)` -> Retorna `6`
  - `fatorial(1)` -> Retorna `1`
  - `fatorial(0)` -> Retorna `1`
  - `fatorial(5)` -> Retorna `120`

#### `exericicio3.py`

**Função `maior_idade`:**

- **Parâmetro**: Uma tupla `pessoa` contendo `(nome, idade)`.
- **Responsabilidades**:
  - Desempacota a tupla para obter `nome` e `idade`.
  - Verifica se a idade é maior ou igual a 18 e imprime a mensagem correspondente.
- **Testes**:
  - `maior_idade(("Calebe", 36))` -> Imprime "Calebe é maior de idade."
  - `maior_idade(("Julia", 15))` -> Imprime "Julia não é maior de idade."

#### `exericico4.py`

**Função `maior_idade`:**

- **Parâmetro**: Uma tupla ou dicionário `pessoa`.
- **Responsabilidades**:
  - Verifica o tipo do argumento e processa adequadamente.
  - Imprime se a pessoa é maior de idade.
- **Testes**:
  - `maior_idade(("Calebe", 36))` -> Imprime "Calebe é maior de idade."
  - `maior_idade({"nome": "Julia", "idade": 15})` -> Imprime "Julia não é maior de idade."

#### `exericio.py`

**Função `primo`:**

- **Parâmetro**: Um número inteiro `n`.
- **Responsabilidades**:
  - Verifica se `n` é primo.
  - Retorna `True` ou `False`.
- **Versão Revisada**:
  - `e_primo(1)` -> Retorna `False`
  - `e_primo(2)` -> Retorna `True`

#### `exericio5.py`

**Função `elemento_na_lista`:**

- **Parâmetros**: Uma lista e um elemento.
- **Responsabilidades**:
  - Realiza busca linear para verificar a presença do elemento.
  - Retorna `True` ou `False`.
- **Testes**:
  - `[1, 2, 3, 4]` e `3` -> Retorna `True`
  - `[1, 2, 3, 4]` e `5` -> Retorna `False`
  - `["a", "b", "c"]` e `"b"` -> Retorna `True`
  - `["a", "b", "c"]` e `"d"` -> Retorna `False`

### Exemplos de Uso

```python
# Exemplo de uso da função maior_numero
from exercicio2 import maior_numero
print(maior_numero([10, 20, 30, 25]))  # Saída: (2, 30)

# Exemplo de uso da função fatorial
from exercicio6 import fatorial
print(fatorial(5))  # Saída: 120

# Exemplo de uso da função maior_idade com tupla
from exericicio3 import maior_idade
maior_idade(("Calebe", 36))  # Saída: Calebe é maior de idade.

# Exemplo de uso da função maior_idade com dicionário
from exericico4 import maior_idade
maior_idade({"nome": "Julia", "idade": 15})  # Saída: Julia não é maior de idade.

# Exemplo de uso da função e_primo (versão revisada)
from exericio import e_primo
print(e_primo(7))  # Saída: True

# Exemplo de uso da função elemento_na_lista
from exericio5 import elemento_na_lista
print(elemento_na_lista([1, 2, 3, 4], 3))  # Saída: True
```

### Boas Práticas e Dicas para Contribuir

1. **Fork e Clone**: Faça um fork do repositório e clone-o em sua máquina local.
2. **Ambiente Virtual**: Use um ambiente virtual para evitar conflitos de dependências.
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows use `venv\Scripts\activate`
   ```
3. **Padrões de Codificação**: Siga o PEP 8, o guia de estilo para Python.
4. **Testes**: Adicione testes para qualquer nova funcionalidade ou correção de bug.
5. **Documentação**: Documente funções e classes com docstrings.
6. **Pull Requests**: Faça pull requests com mensagens claras e concisas, descrevendo o que foi alterado.

### Contribuindo

Para contribuir com este projeto, siga os passos abaixo:

1. Clone o repositório.
2. Crie um branch para sua funcionalidade ou correção (`git checkout -b feature/YourFeature`).
3. Faça commit das suas alterações (`git commit -am 'Adiciona sua funcionalidade'`).
4. Faça push para o branch (`git push origin feature/YourFeature`).
5. Abra um pull request.

### Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

### Contato

Para dúvidas e sugestões, entre em contato através de calebewerneck@hotmail.com

---

Espero que este README.md forneça todas as informações necessárias para entender e contribuir com o projeto. Se precisar de mais detalhes ou tiver outras questões, sinta-se à vontade para perguntar!
