from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS

app = Flask(__name__)
mongo = PyMongo(app, uri="mongodb://localhost:27017/mydatabase")


# Enable CORS for all routes
CORS(app)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    name = data.get('name')
    email = data.get('email')

    if name and email:
        mongo.db.submissions.insert_one({'name': name, 'email': email})
        return jsonify({'message': 'Form submitted successfully!'}), 200
    return jsonify({'message': 'Invalid input!'}), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)  # Make the server accessible externally
