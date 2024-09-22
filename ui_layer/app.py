from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route('/')
def calculator():
    return render_template('calculator.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5003')