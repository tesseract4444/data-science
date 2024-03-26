from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def route_index():
    return 'Index'

@app.route('/test')
def route_test():
    return render_template('02_test.html')
