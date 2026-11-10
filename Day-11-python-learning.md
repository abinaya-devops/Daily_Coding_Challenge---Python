Day 11 – Python Learning

🃏 Challenge: Counting Cards

Problem Statement

Given an integer representing the number of cards selected from a standard deck of 52 playing cards, calculate the number of unique combinations.

The order of selected cards does not matter.

💻 Python Solution

from math import factorial

def combinations(cards):
    total_cards = 52

    result = factorial(total_cards) // (
        factorial(cards) * factorial(total_cards - cards)
    )

    return result

📚 Concepts Learned

1. Combinations: Finding the number of ways to select items when order does not matter.
2. Factorial (!): Multiplying a positive integer by all positive integers below it.
3. math Module: Using Python's built-in math module.
4. factorial(): Calculating factorial values.
5. Integer Division (//): Performing division and returning an integer result.
6. Mathematical Formula: Applying the combination formula (nCr).

🧠 What I Understood

- Selecting A and B is the same as selecting B and A.
- Order does not matter in combinations.
- A standard deck contains 52 cards.
- Factorial is used to calculate the number of possible combinations.
- The number of selected cards determines the result.

🔍 Example Results

Input| Expected Output
combinations(52)| 1
combinations(1)| 52
combinations(2)| 1326
combinations(5)| 2598960
combinations(10)| 15820024220
combinations(50)| 1326

🎯 Learning Outcome

Learned the basic concept of combinations, factorial calculations, and how mathematical formulas can be implemented using Python.

Platform: freeCodeCamp
Language: Python
Challenge: Counting Cards
