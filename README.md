# README.md for Python Exercises Repository

## Overview

This repository consists of several Python scripts, each demonstrating different basic programming concepts, including recursion, conditionals, loop operations, and type handling. These scripts are simple yet instructive examples meant for educational purposes to understand Python syntax and basic programming techniques.

## Project Structure

```
/
|-- exercicio.py          # Checks if a number is prime
|-- exercicio2.py         # Finds the largest number in a list
|-- exercicio3.py         # Check if a person is of legal age
|-- exercicio4.py         # Handle different data structures for age checking
|-- exercicio5.py         # Manual element presence check in list
|-- exercicio6.py         # Calculates the factorial of a number
```

## Languages Used

- Python 3

## Dependencies and Installation

No external dependencies are required for this project as it uses only the Python Standard Library. To run these scripts, you need to have Python 3.x installed. You can download and install Python from https://www.python.org/downloads/.

## Running the Project and Executing Tests

To run any script in the repository, use the following command in your terminal:

```bash
python <script_name>.py
```

Replace `<script_name>` with the name of the script you wish to run. For example, to run the factorial calculator script:

```bash
python exercicio6.py
```

Each script is standalone and provides immediate output upon execution, demonstrating the concepts it is meant to illustrate.

## Detailed File Descriptions

### `exercicio.py`
- **Function: `primo(n)`**
  - Responsible for checking if a given number `n` is a prime.
  - Prints directly whether the number is prime or not, based on mathematical definitions of primality.

### `exercicio2.py`
- **Function: `maior_numero(lista)`**
  - Finds and returns the index and value of the largest number in a provided list of integers.
  - Handles edge cases, like empty lists.

### `exercicio3.py`
- **Function: `maior_idade(pessoa)`**
  - Checks if a person (represented as a tuple of name and age) is of legal age.
  - Utilizes Python’s tuple unpacking feature for readable and concise code.

### `exercicio4.py`
- **Function: `maior_idade(pessoa)`**
  - Overloaded function to handle both tuples and dictionaries representing a person.
  - Demonstrates how to handle different data structures within a single function.

### `exercicio5.py`
- **Function: `elemento_na_lista(lista, elemento)`**
  - Checks for the presence of an element in a list without using the `in` operator.
  - Utilizes a for-loop to iterate through the list, showing the manual method of element lookup.

### `exercicio6.py`
- **Function: `fatorial(n)`**
  - Calculates the factorial of a non-negative integer using recursion.
  - Includes error handling for negative inputs by raising an exception.

## Examples of Use

Each script includes direct examples or test calls within the code. Please refer to the initial explanations within each script for specific examples.

## Contributing

This is a learning and demonstration project, so contributions that improve readability, educational value, or demonstrate additional basic Python concepts are welcome. Please ensure:

- Each contribution is accompanied by comments explaining the changes.
- Consistency in style and naming conventions with existing scripts.
- All changes are fully tested to ensure they work as expected.

For significant changes or new features, please open an issue first to discuss what you would like to add or change. Contributions should be made via pull requests.
