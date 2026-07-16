def calculate(first_number, second_number, operation):
    """
    Perform a mathematical operation on two numbers.

    Parameters:
        first_number (float): The first input number.
        second_number (float): The second input number.
        operation (int): The operation selected by the user.

    Returns:
        float: Result of the selected operation.

    Raises:
        ValueError: If the operation is invalid.
        ZeroDivisionError: If division by zero is attempted.
    """

    if operation == 1:
        return first_number + second_number

    if operation == 2:
        return first_number - second_number

    if operation == 3:
        return first_number * second_number

    if operation == 4:
        if second_number == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")

        return first_number / second_number

    raise ValueError("Invalid operation. Select a number from 1 to 4.")


def main():
    """Take user input and display the calculation result."""

    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    try:
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))
        operation = int(input("Enter your choice (1-4): "))

        result = calculate(first_number, second_number, operation)

        print(f"Result: {result}")

    except ValueError as error:
        print(f"Input error: {error}")

    except ZeroDivisionError as error:
        print(f"Calculation error: {error}")


if __name__ == "__main__":
    main()