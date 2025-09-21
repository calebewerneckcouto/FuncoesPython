# README.md for Python Utility Functions Repository

## Overview

This repository contains a collection of Python utility functions designed to perform various tasks such as identifying the largest number in a list, calculating factorial numbers, checking if an individual is of legal age, verifying prime numbers, and checking list membership without using the `in` operator. The repository is structured to serve as a learning resource or a starting point for related Python projects.

## Project Structure

The project is organized into individual Python files, each containing specific functions that address various programming tasks:

- `exercicio.py`: Contains a function to check if a number is prime.
- `exercicio2.py`: Includes a function to find the largest number in a list and its index.
- `exercicio3.py`: Provides a function that checks if a person is of legal age based on tuples containing names and ages.
- `exercicio4.py`: Expands `exercicio3` by accepting input as either a tuple or a dictionary to check legal age.
- `exercicio5.py`: Contains a function to check for the presence of an element in a list without using the `in` operator.
- `exercicio6.py`: Implements a function to calculate the factorial of a number using recursion.

## Languages Used

- Python (Version 3.x recommended)

## Dependencies

Python 3.x is required. No external libraries are necessary since all scripts use Python's standard library.

## Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/[username]/python-utility-repository.git
cd python-utility-repository
```

## Running the Projects and Executing Tests

To run any script, use the Python interpreter from the command line:

```bash
python exercicio2.py
python exercicio6.py
```

You can modify the test cases within each file to see different outputs based on the functions' logic.

## Code Files and Their Functionalities

### `exercicio.py`

- **Function `primo(n)`**:
  - **Purpose**: Checks if the number `n` is a prime number.
  - **Implementation**: Iterates over numbers to identify if `n` has divisors other than 1 and itself.

### `exercicio2.py`

- **Function `maior_numero(lista)`**:
  - **Purpose**: Identifies and returns the index and value of the largest number in a list.
  - **Implementation**: Iterates through the list to find the maximum value and its index.

### `exercicio3.py` and `exercicio4.py`

- **Function `maior_idade(pessoa)`**:
  - **Purpose**: Checks if a person is of legal age based on their age provided either in a tuple or a dictionary.
  - **Implementation**: Uses type checking to validate input and determine if the age meets the legal threshold.

### `exercicio5.py`

- **Function `elemento_na_lista(lista, elemento)`**:
  - **Purpose**: Checks for the presence of an element in a list manually.
  - **Implementation**: Iterates over the list and compares each element with the target, returning True if found.

### `exercicio6.py`

- **Function `fatorial(n)`**:
  - **Purpose**: Calculates the factorial of a non-negative integer using recursion.
  - **Implementation**: Leverages base case and recursive case to compute factorial.

## Examples of Use

Refer to the Python scripts for examples embedded as test cases, demonstrating the functionality of each function.

## Contributing

We encourage contributions to improve algorithms or extend functionalities. Please adhere to these guidelines when contributing:
- Follow Python's PEP8 style guide.
- Document new functionalities clearly.
- Write tests for the added functions.

To contribute:
1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/myNewFeature`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/myNewFeature`).
5. Open a new Pull Request.

Explore, learn, and contribute to continue enhancing the capabilities of this Python utility collection!