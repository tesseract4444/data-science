from typing import Dict
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/customers')
def route_customers():
    customers: List[str] = ['Jack', 'James', 'Jason', 'John']
    return render_template('11_erben_template.html', customers=customers)