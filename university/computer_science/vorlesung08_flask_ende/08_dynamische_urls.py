from typing import List
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/products/<int:product_id>')
def route_product_by_id(product_id: int):
    product = find_product_by_id(product_id)
    return render_product("03_products.html", product)


'''#in Template:#sorgt für automatische Durchnummerierung
{% for product in products %}
<p>
<a href="{{ url_for('route_product_by_id', product_id=product.id) }}">
{{ product.id }}. {{ product.name }}
</a>
</p>
{% endfor %}'''
