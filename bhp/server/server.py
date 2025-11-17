from flask import Flask, request, jsonify
from flask_cors import CORS
import util
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})


@app.route("/get_location_names", methods = ["GET"])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route("/predict_home_price", methods = ["POST"])
def predict_home_price():
    location = request.form["location"]
    total_sqft = float(request.form["total_sqft"])
    bath = int(request.form["bath"])
    no_bedrooms = int(request.form["no_bedrooms"])

    response = jsonify({
        "estimated_price": util.predict_price(location, total_sqft, bath, no_bedrooms)
    })
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

if __name__ == "__main__":
    print(f"Starting Python flask server ....")
    app.run(debug=True)