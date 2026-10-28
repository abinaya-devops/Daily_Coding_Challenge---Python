
def navigate(commands):
    history = ["Home"]
    current_index = 0

    for command in commands:
        if command.startswith("Visit "):
            history = history[:current_index + 1]
            page = command.replace("Visit ", "", 1)
            history.append(page)
            current_index = len(history) - 1

        elif command == "Back":
            if current_index > 0:
                current_index = current_index - 1

        elif command == "Forward":
            if current_index < len(history) - 1:
                current_index = current_index + 1

    return history[current_index]
  navigate(["Visit About Us", "Visit Visit Us", "Forward", "Visit Contact Us", "Back"])
