from flask import Flask, request, jsonify
import jwt
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    token = jwt.encode({'user': data['username'], 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)},
                       app.config['SECRET_KEY'], algorithm='HS256')
    return jsonify({'token': token})

if __name__ == '__main__':
    app.run(port=5001)
