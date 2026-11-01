def get_value(letter):
    if letter.islower():
        return ord(letter) - 96
    elif letter.isupper():
        return ord(letter) - 38
    else:
        return 0


def verify(message, key, signature):
    message_total = 0

    for letter in message:
        message_total = message_total + get_value(letter)

    key_total = 0

    for letter in key:
        key_total = key_total + get_value(letter)

    total = message_total + key_total

    return total == signature
