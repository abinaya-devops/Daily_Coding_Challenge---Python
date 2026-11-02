import math

def infected(days):
    computers = 1

    for day in range(1, days + 1):
        computers = computers * 2

        if day % 3 == 0:
            patched = math.ceil(computers * 0.20)
            computers = computers - patched

    return computers
