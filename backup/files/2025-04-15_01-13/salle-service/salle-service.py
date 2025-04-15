from flask import Flask, request, jsonify

app = Flask(__name__)

# (remplace par une DB plus tard)
salles = []

@app.route('/salles', methods=['GET'])
def get_salles():
    return jsonify(salles)

@app.route('/salles', methods=['POST'])
def add_salle():
    data = request.json
    nouvelle_salle = {
        "id": len(salles) + 1,
        "nom": data.get("nom"),
        "capacite": data.get("capacite")
    }
    salles.append(nouvelle_salle)
    return jsonify(nouvelle_salle), 201

@app.route('/salles/<int:salle_id>', methods=['DELETE'])
def delete_salle(salle_id):
    global salles
    salles = [s for s in salles if s["id"] != salle_id]
    return jsonify({"message": "Salle supprimée"}), 200

if __name__ == '__main__':
    app.run(port=5002, debug=True)
