from flask import Flask, request, jsonify

app = Flask(__name__)

# Root route to handle both GET and POST methods
@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        return "Hello, World! (GET Request)"
    elif request.method == 'POST':
        return "Hello, World! (POST Request)"

# Webhook route to handle POST requests from Dialogflow
@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    fulfillment_text = "Hello! I am Vishwakarma. How can I assist you?"

    return jsonify({
        "fulfillmentText": fulfillment_text
    })

if __name__ == '__main__':
    app.run(debug=True)
