# Numerology Module

A lightweight Python library for calculating common numerology numbers: Life‑Path, Past, and Future numbers. The core algorithm reduces numbers to a single digit, preserving the master numbers 11, 22, and 33.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Calculate Life‑Path Number](#calculate-life%E2%80%91path-number)
  - [Calculate Past Number](#calculate-past-number)
  - [Calculate Future Number](#calculate-future-number)
- [API Reference](#api-reference)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Features

Compute the Life‑Path number from a full birthdate.
Compute Past and Future numbers from arbitrary integers.
Handles master numbers (11, 22, 33) according to standard numerology practice.
Pure‑Python implementation with no external dependencies.

## Installation

```
# Clone the repository (if hosted on GitHub)

git clone https://github.com/yourusername/numerology-module.git
cd numerology-module

# Optionally install in editable mode for development

pip install -e .
```

> **Note:** The module consists only of a single Python file, so you can also copy numerology.py directly into your project and import the functions.

## Usage

```
from numerology import (
calculate_life_path,
calculate_past_number,
calculate_future_number,
)

# Example 1: Life‑Path number from a birthdate

life_path = calculate_life_path(1990, 7, 15) # => 5
print(f"Life‑Path number: {life_path}")

# Example 2: Past number from an arbitrary integer

past = calculate_past_number(27) # => 9
print(f"Past number: {past}")

# Example 3: Future number from month and day

future = calculate_future_number(7, 15) # => 4
print(f"Future number: {future}")
```

## Calculate Life‑Path Number

```
calculate_life_path(y: int, m: int, d: int) -> int
```

Combines the year, month, and day into a single integer, then reduces it to a single digit or master number.

## Calculate Past Number

```
calculate_past_number(d: int) -> int
```

Reduces any integer d (e.g., a day) to a single digit or master number.

## Calculate Future Number

```
calculate_future_number(m: int, d: int) -> int
```

Combines the month and day into a single integer, then reduces the result. If m equals d and both are 1‑3, the function returns their sum (a special case for early‑stage numerology calculations).

## API Reference

| Function                            | Signature                         | Returns                 | Description                                                                     |
| ----------------------------------- | --------------------------------- | ----------------------- | ------------------------------------------------------------------------------- |
| `calculate_life_path`               | `(y: int, m: int, d: int) -> int` | `int` (1‑9, 11, 22, 33) | Computes Life‑Path number from a full birthdate.                                |
| `calculate_past_number`             | `(d: int) -> int`                 | `int` (1‑9, 11, 22, 33) | Reduces an arbitrary integer to a numerology digit.                             |
| `calculate_future_number`           | `(m: int, d: int) -> int`         | `int` (1‑9, 11, 22, 33) | Reduces the concatenated month/day (or other pair) to a digit.                  |
| `__reduce_to_one_digit` _(private)_ | `(n: int) -> int`                 | `int` (1‑9, 11, 22, 33) | Core reduction loop; sums digits until a single digit or master number remains. |
| `__digit_sum` _(private)_           | `(n: int) -> int`                 | `int`                   | Returns the sum of the decimal digits of `n`.                                   |

## Testing

The project ships with a **pytest** test suite located in the `tests/` folder.
Running the tests validates the core numerology functions and guards against regressions.

### 1. Install the test requirements

```
# Inside the project root
pip install -r requirements.txt   # if you keep a requirements file
# Or just install pytest directly
pip install pytest
```

### 2. Run the test suite

```
# From the repository root
pytest
```

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests for:

- Bug fixes or edge‑case handling (e.g., invalid dates).
- Additional numerology calculations (e.g., Expression number, Soul Urge number).
- Documentation improvements.

Please follow the existing code style and include unit tests for new functionality.
