# Repositório de Exercícios Python

## 📌 Descrição do Projeto

Este repositório contém uma coleção de exercícios em Python que demonstram diferentes técnicas de programação, manipulação de dados e resolução de problemas computacionais.

## 🌐 Estrutura do Projeto

```
exercicios-python/
│
├── src/
│   ├── exercicio.py         # Verificação de número primo
│   ├── exercicio2.py        # Encontrar maior número em lista
│   ├── exercicio3.py        # Verificação de maioridade (tupla)
│   ├── exercicio4.py        # Verificação de maioridade (flexível)
│   ├── exercicio5.py        # Busca de elemento em lista
│   └── exercicio6.py        # Cálculo de fatorial
│
├── tests/
│   └── test_exercicios.py   # Testes unitários
│
├── requirements.txt          # Dependências do projeto
├── README.md                 # Documentação do projeto
└── .gitignore               # Configurações de ignore do Git
```

## 🛠 Tecnologias e Dependências

- **Linguagem**: Python 3.8+
- **Dependências**: 
  - pytest (para testes unitários)

### Instalação das Dependências

```bash
# Crie um ambiente virtual (opcional, mas recomendado)
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt
```

## 🚀 Como Executar

### Executando os Scripts

```bash
# Exemplo de execução de um script
python src/exercicio.py
```

### Executando Testes

```bash
# Rodar todos os testes
pytest tests/

# Rodar testes de um módulo específico
pytest tests/test_exercicios.py
```

## 📂 Detalhamento dos Módulos

### 1. `exercicio.py`: Verificação de Número Primo
- **Função**: `primo(n)`
- **Objetivo**: Determinar se um número é primo
- **Características**:
  - Verifica primalidade até a raiz quadrada
  - Trata números menores ou iguais a 1

### 2. `exercicio2.py`: Maior Número em Lista
- **Função**: `maior_numero(lista)`
- **Objetivo**: Encontrar posição e valor do maior número
- **Características**:
  - Retorna `(índice, valor)` do maior elemento
  - Trata lista vazia retornando `None`

### 3. `exercicio3.py`: Verificação de Maioridade (Tupla)
- **Função**: `maior_idade(pessoa)`
- **Objetivo**: Verificar maioridade usando tupla
- **Características**:
  - Entrada: tupla `(nome, idade)`
  - Imprime resultado da verificação

### 4. `exercicio4.py`: Verificação de Maioridade (Flexível)
- **Função**: `maior_idade(pessoa)`
- **Objetivo**: Verificar maioridade com entrada flexível
- **Características**:
  - Suporta tuplas e dicionários
  - Tratamento dinâmico de entrada

### 5. `exercicio5.py`: Busca em Lista
- **Função**: `elemento_na_lista(lista, elemento)`
- **Objetivo**: Buscar elemento sem usar `in`
- **Características**:
  - Percorre lista manualmente
  - Retorna booleano

### 6. `exercicio6.py`: Cálculo de Fatorial
- **Função**: `fatorial(n)`
- **Objetivo**: Calcular fatorial recursivamente
- **Características**:
  - Implementação recursiva
  - Tratamento de casos especiais (0, 1, negativos)

## 🤝 Contribuindo

1. Faça um fork do repositório
2. Crie uma branch para sua feature (`git checkout -b feature/nova-funcao`)
3. Commit suas alterações (`git commit -m 'Adiciona nova função'`)
4. Push para a branch (`git push origin feature/nova-funcao`)
5. Abra um Pull Request

### Boas Práticas
- Mantenha o código limpo e comentado
- Adicione testes para novas funcionalidades
- Siga o estilo de código PEP 8

## 📜 Licença

Este projeto está sob licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---

**Desenvolvido com ❤️ por um Desenvolvedor Sênior**