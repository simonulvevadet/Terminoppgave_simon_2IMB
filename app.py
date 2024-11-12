# app.py (Flask backend)
from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

# MySQL database connection i app.py
db = mysql.connector.connect(
    host="localhost",       # Standard MySQL-vertsnavn
    user="root",            # MySQL-brukernavn (erstatt med din bruker om nødvendig)
    password="password",    # MySQL-passord (endre til ditt passord)
    database="bike_workshop" # Navn på databasen
)


@app.route('/add_repair', methods=['POST'])
def add_repair():
    data = request.get_json()
    mechanic_id = data['mechanic_id']
    description = data['description']
    total_price = data['total_price']
    
    cursor = db.cursor()
    query = "INSERT INTO Repairs (mechanic_id, description, total_price) VALUES (%s, %s, %s)"
    cursor.execute(query, (mechanic_id, description, total_price))
    db.commit()
    
    return jsonify({"message": "Repair added successfully"}), 201

@app.route('/repairs', methods=['GET'])
def get_repairs():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Repairs")
    repairs = cursor.fetchall()
    return jsonify(repairs)

if __name__ == '__main__':
    app.run(debug=True)
