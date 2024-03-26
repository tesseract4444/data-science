from typing import List
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/products')
def route_products():
    products: List[str] = ['Apfel', 'Birne', 'Ei']
    #übergebe products an template unter dem namen product_names
    return render_template('07_jinja_example.html', product_names=products)