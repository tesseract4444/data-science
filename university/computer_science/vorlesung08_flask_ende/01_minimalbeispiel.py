from flask import Flask

#Konfiguration des Servers
app = Flask(__name__)


#Defintion einer 'Route'
@app.route('/')
def route_index():
    return 'Hello World!'

#Starten des Servers
if __name__=="__main__":
    app.run()


