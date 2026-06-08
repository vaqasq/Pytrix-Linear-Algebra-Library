# Pytrix

A matrix class built from scratch in Python, with no external dependencies. I wrote this while working through Justin Skycak's "Introduction to Algorithms and Machine Learning" to understand linear algebra through implementation rather than just theory.

## What it does

- Matrix addition, subtraction, scalar multiplication, and matrix multiplication
- Transposition
- Determinant via cofactor expansion (recursive) and via RREF
- Reduced row echelon form
- Matrix inversion via RREF
- Used as the computational backend for a K-means clustering implementation, validated against NumPy

## Why no NumPy

The point of this project was to understand what NumPy does under the hood, not to use it. Every operation is implemented manually using nested loops and Python lists.

## Design decisions

**Readability over speed** - the code is written to be clear and easy to follow. This is a learning project, not a production library.

**Minimal object creation** - helper functions like `calculate_determinant` and `reduced_row_echelon_form_helper` operate directly on raw Python lists instead of creating new Matrix objects. This keeps memory overhead low during recursive operations.

**RREF-based determinant** - the recursive cofactor expansion works but gets slow fast on larger matrices. The RREF-based approach tracks row swaps and pivot values to compute the determinant in one pass, which is significantly more efficient.

**Skipped Strassen's algorithm** - Strassen reduces the theoretical complexity of matrix multiplication but adds implementation complexity, extra memory usage, and numerical stability issues. For a library prioritizing clarity it was not worth the tradeoff.

## What I learned

- How core linear algebra operations work at the algorithmic level
- How RREF can be used to compute both the inverse and determinant of a matrix
- How to structure a Python class with clean method chaining
- How to validate a custom implementation against a reference library like NumPy

## Stack

- Python (no external dependencies)

## Usage

```python
from matrix import Matrix

m = Matrix([[1, 2], [3, 4]])
m.show()
m.transpose().show()
print(m.recursive_determinant())
m.reduced_row_echelon_form().show()
```