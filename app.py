from flask import Flask, request, jsonify, session, redirect

app = Flask(__name__)
app.secret_key = "your_secret_key_here"  # Required for session management

# Dummy user database (Replace this with your real database logic)
users_db = {"testuser": {"id": 1, "username": "testuser", "password": "password123"}}

# Enable session management
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"


# Route for logging in the user
@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    user = users_db.get(username)

    if user and user["password"] == password:
        session["user_id"] = user["id"]  # Store user ID in session
        session["username"] = user["username"]  # Store username in session
        return jsonify({"message": "Login successful"})
    else:
        return jsonify({"error": "Invalid credentials"}), 401


# Route to get the currently logged-in user
@app.route("/current_user", methods=["GET"])
def get_current_user():
    if "user_id" in session:
        return jsonify({"username": session["username"]})
    else:
        return jsonify({"error": "Not logged in"}), 401


# Route to log out the user
@app.route("/logout", methods=["POST"])
def logout():
    session.clear()  # Clear session
    return jsonify({"message": "Logged out successfully"})


if __name__ == "__main__":
    app.run(debug=True)
