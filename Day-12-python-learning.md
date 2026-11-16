Day 11 – Counting Cards

Challenge: Counting Cards
Platform: freeCodeCamp – Daily Coding Challenge (Python)
Date: November 7, 2026 (Completed November 16, 2026)
Status: Completed – 6/6 Tests Passed ✅

Problem Description

Given a standard deck of 52 playing cards, calculate how many unique combinations are possible when selecting a specific number of cards.

The order of the selected cards does not matter.

Concepts Learned

- Combinations: Selecting items where order does not matter.
- Factorial: Multiplying a number by all positive integers below it.
- For Loops: Repeating multiplication using iteration.
- range(): Generating numbers in descending order using a negative step.
- Functions: Creating reusable code using "def".
- Parameters: Passing the number of cards to the function.
- Return: Returning the calculated result.
- Integer Division ("//"): Dividing two numbers and getting an integer result.

Mathematical Approach

Combination formula:

C(n, r) = n! / (r! × (n-r)!)

Where:

- n = Total number of cards (52)
- r = Number of cards selected

Example: Selecting 3 cards.

C(52, 3) = 52! / (3! × 49!)

After factorial cancellation:

C(52, 3) = (52 × 51 × 50) / (3 × 2 × 1)

= 132600 / 6

= 22100

Python Solution

def counting_cards(cards):
    result = 1
    factorial = 1

    for i in range(52, 52 - cards, -1):
        result = result * i

    for i in range(cards, 0, -1):
        factorial = factorial * i

    answer = result // factorial

    return answer


print(counting_cards(3))

Output:

22100

How the Logic Works

1. Initialize "result = 1" to calculate the numerator.
2. Use a "for" loop to multiply the required descending numbers from 52.
3. Initialize "factorial = 1" to calculate the denominator.
4. Use another "for" loop to calculate the factorial of the selected cards.
5. Divide the numerator by the denominator using "//".
6. Return the final combination count.

Important Test Cases

Input| Expected Output
52| 1
1| 52
2| 1326
3| 22100
5| 2598960
10| 15820024220
50| 1326

What I Learned

- Understood the difference between permutations and combinations.
- Learned why order does not matter in combinations.
- Understood how factorial cancellation simplifies calculations.
- Practiced multiplication using "for" loops.
- Learned why "result = 1" is used for multiplication.
- Practiced using dynamic values instead of hardcoding.
- Converted mathematical logic into a Python function.
- Improved problem-solving and debugging skills.

Challenge Result

freeCodeCamp Test Results: 6/6 Passed ✅

Successfully completed the Counting Cards challenge by understanding the mathematical logic and implementing the solution independently.

---

One more step forward in my Python learning journey! 🚀
