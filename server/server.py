from flask import Flask, jsonify
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

# Route to serve the JSON file
@app.route('/api/data')
def serve_data_json():
    # Open the JSON file and load it into a Python dictionary
    with open('Multi_agent/moderator_decision.json', 'r') as json_file:
        data = json.load(json_file)
    return jsonify(data)

@app.route('/conversation')
def serve_conversation_json():
    # Open the JSON file and load it into a Python dictionary
    with open('shared_resources.json', 'r') as json_file:
        conversation = json.load(json_file)
    return jsonify(conversation)

# Home route to test if the server is running
@app.route('/')
def home():
    return jsonify({'message': 'Flask backend is running on localhost!'})

if __name__ == '__main__':
    app.run(debug=True, port=8080)
