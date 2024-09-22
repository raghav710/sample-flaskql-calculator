import sqlite3
from flask import Flask, jsonify, request

from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

def get_db_connection():
    conn = sqlite3.connect('calculator.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/history', methods=['GET', 'OPTIONS'])
@cross_origin()
def get_history():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM history ORDER BY id DESC")
    history = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return history

def add_history(operator, num1, num2, result):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO history (operator, num1, num2, result) VALUES (?, ?, ?, ?)", (operator, num1, num2, result))
    conn.commit()
    conn.close()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5001')