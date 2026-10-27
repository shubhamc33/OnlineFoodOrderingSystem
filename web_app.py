
from flask import Flask, jsonify, request

app = Flask(__name__)

MENU = [
    {"id": 1, "name": "Veg Burger", "price": 80},
    {"id": 2, "name": "Pizza", "price": 150},
    {"id": 3, "name": "Sandwich", "price": 60},
]

@app.route("/")
def home():
    return """
    <h1>Online Food Ordering System</h1>
    <p>Welcome! Our food ordering application is running.</p>
    <h2>Menu</h2>
    <ul>
      <li>Veg Burger - Rs. 80</li>
      <li>Pizza - Rs. 150</li>
      <li>Sandwich - Rs. 60</li>
    </ul>
    <p>Health: <a href="/health">Check application health</a></p>
    """

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

@app.route("/menu")
def menu():
    return jsonify(MENU)

@app.route("/order", methods=["POST"])
def order():
    data = request.get_json(silent=True) or {}
    item_id = data.get("item_id")
    item = next((i for i in MENU if i["id"] == item_id), None)

    if item is None:
        return jsonify({"error": "Invalid item_id"}), 400

    return jsonify({
        "message": "Order placed successfully",
        "item": item["name"],
        "total": item["price"]
    }), 201

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=False)
