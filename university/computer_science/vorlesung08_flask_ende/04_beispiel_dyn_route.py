from flask import Flask

app = Flask(__name__)

@app.route('/<int:id>')
def route_with_int(id: int):
    return "ID: {}".format(id)

@app.route('/<string:my_str>')
def route_with_string(my_str: str):
    return "String: {}".format(my_str)

#Eingabe in Browser: /Vorname%20Nachname