from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector
import json, os

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

# Conexion a la base de datos MySQL
db_config = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", "root123"),
    "database": os.getenv("DB_NAME", "tienda")
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route("/api/", methods=['GET'])
def api_root():
    return jsonify({"message": "API is working"})

@app.route("/api/clientes", methods=['GET'])
def get_clientes():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(clientes)

@app.route("/api/clientes/<int:id>", methods=['GET'])
def get_client(id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM clientes WHERE id=%s", (id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return jsonify(row)
    return jsonify({"error": "Cliente no encontrado"}), 404

@app.route("/clientes", methods=["POST"])
def add_cliente():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO clientes (nombre, email) VALUES (%s,%s)",
                   (data["nombre"], data["email"]))
    conn.commit()
    conn.close()
    return jsonify({"msg": "Cliente agregado"}), 201

@app.route("/clientes/<int:id>", methods=["PUT"])
def update_cliente(id):
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE clientes SET nombre=%s, email=%s WHERE id=%s",
                   (data["nombre"], data["email"], id))
    conn.commit()
    conn.close()
    return jsonify({"msg": "Cliente actualizado"})

@app.route("/clientes/<int:id>", methods=["DELETE"])
def delete_cliente(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM clientes WHERE id=%s", (id,))
    conn.commit()
    conn.close()
    return jsonify({"msg": "Cliente eliminado"})

@app.route("/", methods=['GET'])
def index():
    return "Ready to receive requests"

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug = True)