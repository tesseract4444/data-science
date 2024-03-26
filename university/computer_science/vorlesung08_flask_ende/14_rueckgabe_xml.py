from flask import Flask

app = Flask(__name__)

@app.route('/api/products')
def route_api_customers():
    xml_str: str = """\
<products>
    <product>Banane</product>
    <product>Apple</product>
</customers>"""

    # Durch Setzen von 'Content-Type' erkennt Browser Datentyp
    return xml_str, {'Content-Type': 'application/xml'}