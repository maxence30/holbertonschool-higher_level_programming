# task_04_flask.py

from flask import Flask, jsonify, request

app = Flask(__name__)

# Stockage des utilisateurs en mémoire (vide pour les tests)
users = {}

# Endpoint racine
@app.route("/")
def home():
    return "Welcome to the Flask API!"

# Endpoint pour récupérer tous les noms d'utilisateur
@app.route("/data")
def get_usernames():
    return jsonify(list(users.keys()))

# Endpoint pour vérifier le status
@app.route("/status")
def status():
    return "OK"

# Endpoint pour récupérer un utilisateur par username
@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

# Endpoint pour ajouter un nouvel utilisateur via POST
@app.route("/add_user", methods=["POST"])
def add_user():
    try:
        data = request.get_json()
    except:
        return jsonify({"error": "Invalid JSON"}), 400

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Ajouter l'utilisateur
    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    return jsonify({"message": "User added", "user": users[username]}), 201

# Lancer l'application Flask
if __name__ == "__main__":
    app.run()
