# README.md

## Visão Geral do Projeto

Este repositório contém uma coleção de scripts Python projetados para demonstrar manipulações básicas de dados e lógicas de programação, incluindo busca de maior número em uma lista, cálculo de fatorial, verificação de maioridade, identificação de números primos e verificação de presença de elementos em uma lista.

### Estrutura de Diretórios

```
/
|- exercicio.py
|- exercicio2.py
|- exercicio3.py
|- exercicio4.py
|- exercicio5.py
|- exercicio6.py
```

### Linguagens Utilizadas

- **Python**: Versão 3.8 ou superior.

### Dependências

Este projeto não possui dependências externas.

## Instruções de Instalação

1. Clone o repositório:
   ```bash
   git clone URL_DO_REPOSITORIO
   ```
2. Certifique-se de que o Python 3.8+ está instalado na sua máquina.

## Executando os Scripts e Testes

Cada script pode ser executado diretamente via linha de comando. Por exemplo, para executar o `exercicio2.py`, simplesmente use:

```bash
python exercicio2.py
```

Para executar os exemplos de uso inclusos em cada script ou qualquer teste escrito, você pode iniciar diretamente o script escolhido, visto que os exemplos de uso estão geralmente no final dos scripts como chamadas às funções implementadas.

## Detalhes dos Scripts

### exercicio.py

- **Função**: `primo(n)`
  - **Objetivo**: Verificar se um número inteiro positivo é primo.
  - **Exemplo de Uso**:
    ```python
    primo(7) # Saída: "É primo"
    ```

### exercicio2.py

- **Função**: `maior_numero(lista)`
  - **Objetivo**: Encontrar o maior número numa lista de inteiros e retornar sua posição e valor.
  - **Exemplo de Uso**:
    ```python
    maior_numero([10, 20, 30, 25]) # Saída: (2, 30)
    ```

### exercicio3.py e exercicio4.py

- **Função**: `maior_idade(pessoa)`
  - **Objetivo**: Verificar se uma pessoa é maior de idade (18 anos ou mais) baseado em uma entrada de tupla ou dicionário.
  - **Exemplo de Uso**:
    ```python
    maior_idade(("Calebe", 36)) # Saída: "Calebe é maior de idade."
    maior_idade({"nome": "Julia", "idade": 15}) # Saída: "Julia não é maior de idade."
    ```

### exercicio5.py

- **Função**: `elemento_na_lista(lista, elemento)`
  - **Objetivo**: Verificar a presença de um elemento em uma lista.
  - **Exemplo de Uso**:
    ```python
    elemento_na_lista([1, 2, 3], 3) # Saída: True
    ```

### exercicio6.py

- **Função**: `fatorial(n)`
  - **Objetivo**: Calcular o fatorial de um número inteiro não-negativo.
  - **Exemplo de Uso**:
    ```python
    fatorial(5) # Saída: 120
    ```

## Contribuindo

Contribuições são sempre bem-vindas! Aqui estão algumas formas em que você pode contribuir:
- Criando issues para reportar bugs ou sugerir melhorias.
- Implementando novas funcionalidades ou melhorando a eficiência das existentes.
- Melhorando a documentação ou comentários no código para torná-lo mais compreensível.
- Adicionando testes para garantir a estabilidade do código ao longo das mudanças.

### Boas Práticas

- Siga as convenções de estilo de código PEP8.
- Inclua comentários claros e concisos.
- Escreva testes para verificar as funcionalidades antes de enviar um pull request.
- Leia sempre o que está em aberto em issues e pull requests para evitar trabalho duplicado.
- Mantenha um ambiente cordial e respeite todas as contribuições.

## Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.