from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/customers')
def route_api_customers():
    customers = [
        {'first_name': 'Jason', 'family_name': 'Bourne'},
        {'first_name': 'James', 'family_name': 'Bond'},
        {'first_name': 'Jack', 'family_name': 'Bauer'}
    ]
# Wandelt Argument in JSON um, teilt Browser Datentyp 'application/json' mit
    return jsonify(customers)