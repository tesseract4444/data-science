from flask import Flask

#Konfiguration des Servers
app = Flask(__name__)

#Defintion einer 'Route'
@app.route('/<string:who>')
def route_greet(who: str):
    return "Hallo, {}!".format(who)

if __name__ == "__main__":
    app.run()





"""name = input('Bitte Ihren Namen eingeben...')

#Defintion einer 'Route'
@app.route('/')
def route_index():
    return 'Hallo, ' + name + '!' """