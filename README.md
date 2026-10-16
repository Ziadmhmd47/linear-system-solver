# Gaussian Elimination Solver

## Overview

Gaussian Elimination Solver is a Python application that solves systems of linear equations using the Gaussian Elimination algorithm.

The application provides a graphical user interface (GUI) built with Tkinter and displays the solution process step by step, making it easier to understand matrix operations and how linear systems are solved.

## Features

- Solve systems of linear equations with multiple variables.
- Enter the number of variables and equation coefficients through a graphical interface.
- Display the augmented matrix at each stage of the solution.
- Perform row swapping (pivoting).
- Normalize pivot rows.
- Eliminate variables using elementary row operations.
- Display the final Reduced Row Echelon Form (RREF).
- Show the calculated values of the variables.
- Handle invalid numeric inputs and certain singular matrix cases.

## Technologies Used

- **Python** — Core programming language.
- **NumPy** — Matrix operations and numerical calculations.
- **Tkinter** — Graphical user interface (GUI).

## Algorithm

The application uses Gaussian Elimination with row operations to transform an augmented matrix into Reduced Row Echelon Form (RREF).

The main steps are:

1. Read the coefficients and constants of the equations.
2. Construct the augmented matrix.
3. Select pivots and swap rows when necessary.
4. Normalize pivot rows.
5. Eliminate entries below each pivot.
6. Eliminate entries above each pivot.
7. Display the resulting matrix and the calculated solution.

## Example

Consider the following system of linear equations:

```text
2x + y = 5
x - y = 1
```

The corresponding augmented matrix is:

```text
[ 2   1 | 5 ]
[ 1  -1 | 1 ]
```

The application displays the row operations step by step and calculates the solution:

```text
x = 2
y = 1
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/gaussian-elimination-solver.git
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Navigate to the Project Directory

```bash
cd gaussian-elimination-solver
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python gaussian_elimination.py
```

Make sure Python and Tkinter are installed on your system.

## Learning Objectives

This project demonstrates practical understanding of:

- Gaussian Elimination.
- Augmented matrices and elementary row operations.
- Pivot selection and row swapping.
- Reduced Row Echelon Form (RREF).
- Matrix manipulation using NumPy.
- Building graphical applications with Tkinter.
- Input validation and basic error handling.

## Limitations

- The current implementation is designed primarily for systems with a unique solution.
- Some singular or inconsistent systems may not be classified correctly.
- Numerical precision and very small pivot values may affect the results.

## Project Status

Educational project.
