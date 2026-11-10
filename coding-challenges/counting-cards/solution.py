from math import factorial

def combinations(cards):
    total_cards = 52

    result = factorial(total_cards) // (
        factorial(cards) * factorial(total_cards - cards)
    )

    return result
