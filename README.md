# README.md

## Sobre o Projeto

Este repositório contém uma série de exercícios de Python que ilustram conceitos de programação básicos, tais como busca em listas, cálculo de fatoriais, verificação de idade e primalidade, todos implementados de uma maneira legível e com exemplos de uso claros.

### Estrutura do Projeto

O projeto é organizado conforme a seguir:

    .
    ├── exercicio.py            # Verificação de números primos
    ├── exercicio2.py           # Busca do maior número em uma lista
    ├── exercicio3.py           # Verificação de maioridade
    ├── exercicio4.py           # Verificação de maioridade com suporte a tuplas e dicionários
    ├── exercicio5.py           # Verificação de presença de elemento em lista sem usar 'in'
    ├── exercicio6.py           # Cálculo do fatorial de um número
    └── README.md               # Este arquivo

### Tecnologias Utilizadas

- **Python:** Linguagem de programação usada para todos os scripts nesse repositório.

## Começando

### Pré-requisitos

Para rodar os scripts, você precisará ter Python instalado na sua máquina. Python pode ser baixado através do [site oficial](https://www.python.org/downloads/).

### Instalação

1. Clone o repositório:
   ```sh
   git clone https://your-repository-link-here.com
   ```
2. Nenhuma instalação adicional de pacotes é necessária, pois os scripts usam apenas a biblioteca padrão do Python.

## Uso

Cada um dos arquivos `.py` pode ser executado de forma independente através do seguinte comando:

```sh
python nome_do_arquivo.py
```

Cada script vem com exemplos incorporados, que são executados diretamente ao rodar o arquivo. Para usos específicos, você pode modificar os valores ou as chamadas de função conforme necessário no próprio código.

### Utilizando Funções dos Scripts
Para usar funções específicas em seus próprios projetos Python, você pode importar a função desejada com um comando de importação. Por exemplo, para usar a função `fatorial` do arquivo `exercicio6.py`:
```python
from exercicio6 import fatorial

print(fatorial(5))  # Output: 120
```

## Contribuindo

Contribuições são o que fazem a comunidade de código aberto um lugar tão poderoso para aprender, inspirar e criar. Todas as contribuições que você fizer são **muito apreciadas**.

1. Faça um Fork do projeto
2. Crie sua Feature Branch (`git checkout -b feature/NovaFeature`)
3. Cometa suas mudanças (`git commit -m 'Adicionado alguma NovaFeature'`)
4. Faça o Push para a Branch (`git push origin feature/NovaFeature`)
5. Abra uma Pull Request

## Boas Práticas

- **Legibilidade do Código:** Certifique-se de que seu código é limpo e legível; isso ajuda outros desenvolvedores a entender e manter.
- **Comentários e Documentação:** Forneça comentários claros e uma documentação concisa para explicar o que seu código faz.
- **Adesão ao Padrão:** Siga as convenções de codificação e padrões usados ao longo dos scripts existentes neste repositório.

## Licença

Distribuído sob a Licença MIT. Veja `LICENSE` para mais informações.