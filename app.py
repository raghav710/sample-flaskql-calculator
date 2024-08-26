import sqlite3
from flask import Flask, jsonify, request

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('calculator.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/calculate', methods=['POST'])
def calculate_api():
    data = request.get_json()
    operator = data['operator']
    num1 = data['num1']
    num2 = data['num2']

    result = calculate(operator, num1, num2)

    conn = get_db_connection()
    conn.execute("INSERT INTO history (operator, num1, num2, result) VALUES (?, ?, ?, ?)", (operator, num1, num2, result))
    conn.commit()
    conn.close()

    return jsonify({'result': result})

@app.route('/history', methods=['GET'])
def get_history():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM history")
    history = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return jsonify({'history': history})

if __name__ == '__main__':
    app.run(debug=True)