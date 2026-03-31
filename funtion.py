   
def generic_input(mensage: str, menor: bool, normalized: str | int | float | None = None) -> str | int | float:
    """
    Allows you to create a generic input field that automatically normalizes values.

    Args:

        message (str): The message to be displayed in the input field.
        menor (bool): Validates whether the number is negative or positive
        normalized (int, float, or None): The normalization type to apply to the data; if no value is specified, a default str value is returned.

    Returns:

        result (str, int, or float): The normalized value entered by the user.
    """
    valid = False

    while not valid:
        try:
            user_input = input(mensage).strip().lower()

            if user_input is None:
                print("The answer is empty.")

            if menor:
                if user_input <= 0:
                    print("You cannot enter negative numbers")
                    return user_input
            
            if normalized is None:
                return user_input
            
            if normalized in [str, int, float]:
                return normalized(user_input)
            return normalized(user_input)
        
        except ValueError:
            print("Invalid entry, please try again")


