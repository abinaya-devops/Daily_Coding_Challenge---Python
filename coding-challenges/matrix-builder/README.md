Day 9 – Matrix Builder (November 6, 2026)

🐍 Challenge: Matrix Builder

Problem Statement:

Given two integers representing the number of rows and columns, create and return a matrix (list of lists) filled with zeros.

Example:

Input:

build_matrix(2, 3)

Output:

[
    [0, 0, 0],
    [0, 0, 0]
]

💻 Python Solution

def build_matrix(rows, cols):
    matrix = []

    for i in range(rows):
        row = [0] * cols
        matrix.append(row)

    return matrix

📚 Concepts Learned

- Lists: Creating and storing elements in a list.
- For Loop: Repeating operations based on the number of rows.
- range(): Generating a sequence of numbers to control loop iterations.
- List Multiplication: Using "[0] * cols" to create multiple zeros.
- append(): Adding each row to the matrix.
- return: Returning the complete matrix and ending function execution.

🧠 What I Understood

1. "range(rows)" controls how many times the loop executes.
2. "[0] * cols" creates a row containing the required number of zeros.
3. "append()" adds each newly created row to the matrix.
4. "return matrix" returns the complete matrix after the loop finishes.
5. Using "for i in rows" with an integer causes a TypeError because an integer is not iterable.

🎯 Learning Outcome

Learned how to create a 2D list (matrix) using nested list structures, loops, list multiplication, and the append method.

Platform: freeCodeCamp
Language: Python
Challenge: Matrix Builder
