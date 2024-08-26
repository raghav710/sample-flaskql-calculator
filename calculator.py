import sqlite3

def calculate(operator, num1, num2):
    """Performs a calculation based on the given operator and numbers.

    Args:
        operator (str): The operator to use (e.g., "+", "-", "*", "/").
        num1 (float): The first number.
        num2 (float): The second number.

    Returns:
        float: The result of the calculation.
    """
    num1 = float(num1)
    num2 = float(num2)
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            raise ValueError("Cannot divide by zero.")
        return num1 / num2
    else:
        raise ValueError("Invalid operator.")