from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
# Allow local dev from frontend at http://localhost:3000
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/api", methods=["GET"])
def api_root():
# Example JSON for your /api route
return jsonify({
"service": "flask-backend",
"status": "ok",
"message": "Backend is running"
})


@app.route("/api/submittodoitem", methods=["POST"])
def submit_todo_item():
"""
Expects JSON payload: {"itemName": "...", "itemDescription": "..."}
Returns a success JSON.
"""
data = request.get_json(force=True, silent=True) or {}
item_name = data.get("itemName")
item_description = data.get("itemDescription")


if not item_name:
return jsonify({"ok": False, "error": "itemName is required"}), 400


# Here you could insert into MongoDB if needed.
# For now, just echo back the payload.
return jsonify({
"ok": True,
"message": "Item received",
"data": {
"itemName": item_name,
"itemDescription": item_description
}
}), 201


if __name__ == "__main__":
# Run on 0.0.0.0 so it's reachable inside Docker
app.run(host="0.0.0.0", port=5000, debug=True)