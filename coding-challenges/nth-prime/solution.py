def is_prime(number):
    for divisor in range(2, number):
        if number % divisor == 0:
            return False

    return True


def nth_prime(n):
    count = 0
    candidate = 2

    while count < n:
        if is_prime(candidate):
            count = count + 1

        candidate = candidate + 1

    return candidate - 1
