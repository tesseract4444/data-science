from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def route_index():
    return render_template('06_index.html')