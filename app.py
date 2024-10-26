from flask import Flask, jsonify, request, abort
from pymongo import MongoClient
from bson import ObjectId
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

client = MongoClient('mongodb+srv://italocajado:ES6pyI4n7XG43rSL@cluster0.ttz2o.mongodb.net/')
db = client['mydatabase']
collection = db['users']

@app.route('/users', methods=['GET'])
def getUsers():
    users = list(collection.find())
    for user in users:
        user['_id'] = str(user['_id'])
    return jsonify(users)

@app.route('/users', methods=['POST'])
def createUser():
    data = request.json
    userId = collection.insert_one(data).inserted_id
    return jsonify({'_id': str(userId)}), 201

@app.route('/users/<id>', methods=['PUT'])
def updateUser(id):
    data = request.json
    result = collection.update_one({'_id': ObjectId(id)}, {'$set': data})
    if result.modified_count == 0:
        abort(404)
    return jsonify({"message": "User updated successfully"})

@app.route('/users/<id>', methods=['DELETE'])
def deleteUser(id):
    result = collection.delete_one({'_id': ObjectId(id)})
    if result.deleted_count == 0:
        abort(404)
    return jsonify({"message": "User deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)
