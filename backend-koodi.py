from flask import Flask, jsonify

app = Flask(__name__)

# Testidata vapaista huoneista
huoneet = [
    {"huone": 101, "tyyppi": "1hh Standard", "hinta": "85e/yö", "tila": "Vapaa"},
    {"huone": 204, "tyyppi": "2hh Superior", "hinta": "120e/yö", "tila": "Vapaa"},
    {"huone": 301, "tyyppi": "Sviitti", "hinta": "250e/yö", "tila": "Vapaa"}
]

@app.route('/api/huoneet', methods=['GET'])
def hae_huoneet():
    return jsonify(huoneet)

if __name__ == '__main__':
    app.run(debug=True)