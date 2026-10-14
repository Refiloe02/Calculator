# Python Calculator

A simple graphical calculator built with Python and Tkinter. This project was created to practise Python programming, GUI development, and unit testing.

## Features

- Addition, subtraction, multiplication, and division
- Decimal number support
- Percentage calculations
- Positive and negative number conversion
- Square root calculations
- Clear button to reset the calculator
- Error handling for division by zero
- Unit tests using Python's `unittest` framework

## Technologies Used

- **Python 3** — programming language
- **Tkinter** — graphical user interface
- **Math** — square root calculations
- **Unittest** — unit testing

## Getting Started

### Prerequisites

Make sure Python 3 is installed on your computer.

Check your Python version:

```bash
python3 --version
```

Tkinter is included with many Python installations. On Ubuntu-based systems, if it is missing, install it with:

```bash
sudo apt install python3-tk
```

### Installation

1. Clone this repository:

   ```bash
   git clone YOUR_REPOSITORY_URL
   ```

2. Navigate to the project directory:

   ```bash
   cd Calculator
   ```

### Run the Calculator

Start the graphical calculator with:

```bash
python3 calculator.py
```

Replace `calculator.py` with the actual filename of your calculator script if it is different.

## Running the Tests

Run the unit tests with:

```bash
python3 -m unittest test_calculator.py
```

To see the name and result of each test, use:

```bash
python3 -m unittest -v test_calculator.py
```

The tests cover basic arithmetic operations, decimal calculations, square roots, percentages, sign changes, and division-by-zero behaviour.

## What I Learned

Through this project, I practised:

- Creating a graphical interface with Tkinter.
- Using lists and nested loops to generate calculator buttons.
- Handling button clicks with functions and lambda expressions.
- Using conditional statements to process calculator operations.
- Working with Python's `math` module.
- Writing and running unit tests with `unittest`.

## Future Improvements

- Improve error handling and calculator reset behaviour.
- Support consecutive calculations.
- Expand unit tests to test the calculator's actual calculation logic.


