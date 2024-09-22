import sqlite3

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app, origins="http://localhost:5003")

@app.route('/calculate', methods=['POST'])
@cross_origin()
def calculate_result():
    data = request.get_json()
    operator = data['operator']
    num1 = data['num1']
    num2 = data['num2']

    result = calculate(operator, num1, num2)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

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