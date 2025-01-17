from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/users', methods=['GET'])
def get_data():
    return jsonify({'payload':'success'})


@app.route('/user', methods=['POST'])
def post_data():
    return jsonify({'payload':'success'})


@app.route('/user', methods=['DELETE'])
def delete_data():
    return jsonify({'payload':'success'})


@app.route('/user', methods=['PUT'])
def put_data():
    
    if request.method == 'PUT':
        return jsonify({'payload':'success', 'error' : False}), 200
    else:
        return jsonify({'error' : 'metodo no aceptado'}), 405


@app.route('/api/v1/users', methods=['GET'])
def get_2_data():
    return jsonify({'payload':[]})


@app.route('/api/v1/user', methods=['POST'])
def post_2_data():
    email = request.args.get('email')
    name = request.args.get('name')
    return jsonify({'payload': {
        'email': email,
        'name': name,
    }})
    
    
@app.route('/api/v1/user/add', methods=['POST'])
def post_3_data():
    email = request.form.get('email')
    name = request.form.get('name')
    id = request.form.get('id')
    return jsonify({'payload': {
        'email': email,
        'name': name,
        'id': id,
    }})


@app.route('/api/v1/user/create', methods=['POST'])
def post_4_data():
    
    dato = request.get_json()
    
    email = dato.get('email')
    name = dato.get('name')
    id = dato.get('id')
    return jsonify({'payload':{ 
        'email':email,
        'name': name,
        'id': id,
    }})
    

if __name__ == "__main__":
    app.run(debug=True)