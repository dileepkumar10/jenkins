from flask import Flask, request, jsonify
app=Flask(__name__)
@app.route('/')
def home():
    return "welcome to simple calculater!"
@app.route('/calculate', method=['POST'])
def calculate():
    data = request.get_json()
    operation = data.get('operation')
    num1 = data.get('num1')
    num2 = data.get('num2')
    
    if not all([operation,num1,num2]):
        return jsonify({"error":"Please provide an operation and two numbers"}), 400
    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return jsonify({"error": "Division by zero is not allowed"}), 400
        result = num1 / num2
    else:
        return jsonify({"error": "Invalid operation"}), 400
    
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
     