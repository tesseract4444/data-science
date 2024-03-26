from flask import Flask, render_template

app = Flask(__name__)

@app.route('/products/<int:id>')
def route_product_by_id(id: int):
    product: Product = find_product_by_id(id)
    return render_template('03_products.html', product)

