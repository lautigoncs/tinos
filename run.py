import os
from flask import Flask, session
from route import route
 
def main():
    app = Flask(__name__,template_folder='templates',static_folder='static')
    app.config['SECRET_KEY'] = '2948167968'  
    route(app)
    app.run('0.0.0.0', 5000, debug=True) 
main()

# Créditos a MARIANO TRIGILA por la integracion de Python con MySQL
# Muchas gracias!