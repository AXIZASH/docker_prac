import sys
sys.path.insert(0, "/app/deps")
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/calculate", methods=["GET","POST"])
def calculate():
    if request.method == "GET":
        return jsonify({"message": "Use POST with JSON data"}), 200
    
    data = request.get_json()
    num1 = data.get("num1")
    num2 = data.get("num2")
    operation = data.get("operation")

    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return jsonify({"error": "Division by zero is not allowed"}), 400
        result = num1 / num2
    else:
        return jsonify({"error": "Invalid operation"}), 400

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
