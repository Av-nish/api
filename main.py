from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="Hello, this is a basic Flask API!")

@app.route('/hello', methods=['POST'])
def hello():
    data = request.get_json()
    if data and data.get('message') == 'hello':
        return jsonify(response="hi")
    else:
        return jsonify(response="You can only say 'hello"), 400

if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=5005)