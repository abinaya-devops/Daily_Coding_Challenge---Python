def spookify(boo):
    boo = boo.replace("_", "~")
    boo = boo.replace("-", "~")

    result = ""
    letter_count = 0

    for letter in boo:
        if letter == "~":
            result = result + letter
            continue

        if letter_count % 2 == 0:
            result = result + letter.upper()
        else:
            result = result + letter.lower()

        letter_count = letter_count + 1

    return result
