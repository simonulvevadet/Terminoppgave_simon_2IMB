# app.py (Flask backend)
from flask import Flask, jsonify, request, render_template
import mysql.connector

app = Flask(__name__,
            static_url_path='', 
            static_folder='Static',
            template_folder='Templates')

# MySQL database connection i app.py
db = mysql.connector.connect(
    host="localhost", # Standard MySQL host navn
    user="root", # MySQL brukernavn 
    password="password", # MySQL passord 
    database="bike_workshop" # Navn på databasen
)


@app.route('/search_query', methods=['POST'])
def search_query():
    data = request.get_json()
    search = data['search']
    search = int(search)
    
    cursor = db.cursor(dictionary=True)
    query = "SELECT * FROM Repairs WHERE id = %s"
    cursor.execute(query, (search))
    results = cursor.fetchall()
    return jsonify(results)

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

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search.html')
def search():
    return render_template('search.html')

if __name__ == '__main__':
    app.run(debug=True)
