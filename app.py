from flask import Flask, render_template, jsonify
import mysql.connector
from flask_cors import CORS

app = Flask(__name__, static_folder="assets", template_folder="pages")
CORS(app)

# Conectar con MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",  # Cambialo si usás otro usuario
    password="GonzalO22@",
    database="hamburgueseria"
)
cursor = db.cursor(dictionary=True)

# 📌 Ruta para servir la página principal
@app.route('/')
def index():
    return render_template('index.html')

# 📌 Ruta API para obtener productos en formato JSON
@app.route('/productos', methods=['GET'])
def get_productos():
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    return jsonify(productos)

if __name__ == '__main__':
    app.run(debug=True)

