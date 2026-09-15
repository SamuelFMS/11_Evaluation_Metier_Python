def input_number(message: str, min: int, max: int) -> int:
    try:
        saisie = int(input(message))
        if saisie >= min and saisie <= max:
            return saisie
        else:
            return input_number(message, min, max)
    except ValueError:
        print("Incorrect input. Please enter a number")
        return input_number(message, min, max)