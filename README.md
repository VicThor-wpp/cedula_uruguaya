
# CedulaUruguaya

The `CedulaUruguaya` package provides a set of tools for managing and validating Uruguayan ID numbers (Cédulas de Identidad). It includes functions to validate these IDs, calculate verification digits, format them in a standard way, and more. This package aims to simplify operations related to Uruguayan IDs in various applications, from data validation to user interface enhancements.

## Features

### `get_validation_digit(ci)`
Calculates the verification digit for a given Uruguayan ID number (without the verification digit).

- **Parameters**:
  - `ci` (int): The ID number without its last verification digit.

- **Returns**:
  - `int`: The calculated verification digit.

- **Example**:
  ```python
  print(CedulaUruguaya.get_validation_digit(3298763))  # Output: 4
  ```

### `clean_ci(ci)`
Cleans an ID number by removing non-numeric characters such as dots and dashes.

- **Parameters**:
  - `ci` (str/int): The ID number as a string or integer, potentially formatted with dots or dashes.

- **Returns**:
  - `int`: The cleaned numeric ID.

- **Example**:
  ```python
  print(CedulaUruguaya.clean_ci("3.298.763-4"))  # Output: 32987634
  ```

### `validate_ci(ci)`
Validates a complete Uruguayan ID number by comparing its last digit against the calculated verification digit.

- **Parameters**:
  - `ci` (str/int): The complete ID number.

- **Returns**:
  - `bool`: `True` if the ID is valid, `False` otherwise.

- **Example**:
  ```python
  print(CedulaUruguaya.validate_ci("3.298.763-4"))  # Output: True
  ```

### `format_ci(ci)`
Formats an ID number into a more visually friendly format (`X.XXX.XXX-X`).

- **Parameters**:
  - `ci` (int/str): The ID number to format.

- **Returns**:
  - `str`: The formatted ID.

- **Example**:
  ```python
  print(CedulaUruguaya.format_ci(32987634))  # Output: '3.298.763-4'
  ```

### `random_ci_in_range(start, end)`
Generates a random Uruguayan ID number within a specified range, including the verification digit.

- **Parameters**:
  - `start` (int): Lower bound of the ID range.
  - `end` (int): Upper bound of the ID range.

- **Returns**:
  - `int`: A valid ID number.

- **Example**:
  ```python
  print(CedulaUruguaya.random_ci_in_range(1000000, 2000000))
  ```

### `international_format(ci)`
Converts a local ID format to an international format prefixed with `UY-`.

- **Parameters**:
  - `ci` (int/str): The ID number.

- **Returns**:
  - `str`: The internationally formatted ID.

- **Example**:
  ```python
  print(CedulaUruguaya.international_format(32987634))  # Output: 'UY-3.298.763-4'
  ```

### `bulk_validate_ci(ci_list)`
Validates a list of IDs in one operation, returning a dictionary with the IDs and their validation results.

- **Parameters**:
  - `ci_list` (list): A list of complete ID numbers.

- **Returns**:
  - `dict`: A dictionary with IDs as keys and validation results (`True` or `False`) as values.

- **Example**:
  ```python
  print(CedulaUruguaya.bulk_validate_ci(["3.298.763-4", "1.234.567-8"]))
  ```

## Installation

To install the `CedulaUruguaya` package, run the following command:

```bash
pip install cedula_uruguaya
```

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
