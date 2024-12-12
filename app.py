# app.py (Flask backend)
from flask import Flask, jsonify, request, render_template  # Importerer nødvendige Flask-moduler for å lage API-et og håndtere forespørsler.
import mysql.connector  # Importerer MySQL-modulen for databaseforbindelse.

app = Flask(__name__,
            static_url_path='',  # Setter standard statisk URL-bane.
            static_folder='Static',  # Angir mappen for statiske filer.
            template_folder='Templates')  # Angir mappen for HTML-maler.

# MySQL database connection i app.py
db = mysql.connector.connect(
    host="localhost",  # Standard MySQL host-navn.
    user="root",  # MySQL brukernavn (standard er 'root').
    password="password",  # MySQL-passord (endre for å matche din lokale databasekonfigurasjon).
    database="bike_workshop"  # Navn på databasen som brukes i applikasjonen.
)

@app.route('/search_query', methods=['POST'])  # Definerer en rute for POST-forespørsler til '/search_query'.
def search_query():
    data = request.get_json()  # Henter JSON-data fra forespørselen.
    search = data['search']  # Henter 'search'-verdien fra dataene.
    search = int(search)  # Konverterer søkeverdien til et heltall.
    
    cursor = db.cursor(dictionary=True)  # Oppretter en databasekursor som returnerer resultater som ordbøker.
    query = "SELECT * FROM Repairs WHERE id = %s"  # SQL-spørring for å finne reparasjoner med spesifikt ID.
    cursor.execute(query, (search,))  # Utfører SQL-spørringen med søkeverdien som parameter.
    results = cursor.fetchall()  # Henter alle resultater fra spørringen.
    return jsonify(results)  # Returnerer resultatene som JSON-respons.

@app.route('/add_repair', methods=['POST'])  # Definerer en rute for POST-forespørsler til '/add_repair'.
def add_repair():
    data = request.get_json()  # Henter JSON-data fra forespørselen.
    mechanic_id = data['mechanic_id']  # Henter 'mechanic_id' fra dataene.
    description = data['description']  # Henter 'description' fra dataene.
    total_price = data['total_price']  # Henter 'total_price' fra dataene.
    
    cursor = db.cursor()  # Oppretter en databasekursor.
    query = "INSERT INTO Repairs (mechanic_id, description, total_price) VALUES (%s, %s, %s)"  # SQL-spørring for å legge til en ny reparasjon.
    cursor.execute(query, (mechanic_id, description, total_price))  # Utfører spørringen med verdiene som parametere.
    db.commit()  # Lagrer endringene i databasen.
    
    return jsonify({"message": "Repair added successfully"}), 201  # Returnerer en suksessmelding med statuskode 201.

@app.route('/repairs', methods=['GET'])  # Definerer en rute for GET-forespørsler til '/repairs'.
def get_repairs():
    cursor = db.cursor(dictionary=True)  # Oppretter en databasekursor som returnerer resultater som ordbøker.
    cursor.execute("SELECT * FROM Repairs")  # SQL-spørring for å hente alle reparasjoner.
    repairs = cursor.fetchall()  # Henter alle resultater fra spørringen.
    return jsonify(repairs)  # Returnerer reparasjonene som JSON-respons.

@app.route('/')  # Definerer rot-ruten ('/') for applikasjonen.
def home():
    return render_template('index.html')  # Render HTML-filen 

@app.route('/Insert.html')
def insert():
    return render_template('Insert.html')# Render HTML-filen 

@app.route('/Varer.html')
def varer():
    return render_template('Varer.html')# Render HTML-filen 

@app.route('/search.html')  # Definerer en filen
def search():
    return render_template('search.html')  # Render HTML-filen 'search.html'.

if __name__ == '__main__':  # Sjekker om skriptet kjøres direkte.
    app.run(debug=True)  # Starter Flask-applikasjonen med debug-modus aktivert.

@app.route('/delete_repair', methods=['POST'])  # Definerer en rute for POST-forespørsler til '/delete_repair'.
def delete_repair():
    print("stempel1")  # Debugging-utskrift for å spore kjøring.
    data = request.get_json()  # Henter JSON-data fra forespørselen.
    repair_id = data['repairId']  # Henter 'repairId' fra dataene.
    print("stempel2")  # Debugging-utskrift for å spore kjøring.
    print(repair_id)  # Skriver ut ID-en som skal slettes for debugging.
    
    cursor = db.cursor()  # Oppretter en databasekursor.
    query = "DELETE FROM Repairs WHERE id = %s"  # SQL-spørring for å slette en reparasjon med spesifikt ID.
    print(query)  # Skriver ut SQL-spørringen for debugging.
    cursor.execute(query, (repair_id,))  # Utfører spørringen med ID-en som parameter.
    db.commit()  # Lagrer endringene i databasen.
    return jsonify({"message": f"Repair with ID {repair_id} deleted successfully"}), 200  # Returnerer en suksessmelding.

if __name__ == '__main__':  # Sjekker om skriptet kjøres direkte.
    app.run(debug=True)  # Starter Flask-applikasjonen med debug-modus aktivert.
