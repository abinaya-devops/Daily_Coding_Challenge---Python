def counting_cards(cards):
    result = 1
    factorial = 1

    for i in range(52, 52 - cards, -1):
        result = result * i

    for i in range(cards, 0, -1):
        factorial = factorial * i

    answer = result // factorial

    return answer
