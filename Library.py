# Importer nødvendige moduler fra Flask for å lage en webapplikasjon
from flask import Flask, jsonify, request, render_template, redirect, url_for
# Importer MySQL-connector for å kommunisere med en MySQL-database
import mysql.connector

# Opprett en instans av Flask-klassen for webapplikasjonen
app = Flask(__name__,
            static_url_path='',  # Angir URL-sti for statiske filer (f.eks. CSS, JS, bilder)
            static_folder='Static',  # Mappe for statiske filer
            template_folder='Templates')  # Mappe for HTML-malene

# Oppsett for tilkobling til MySQL-databasen
db = mysql.connector.connect(
    host="localhost",       # Vert der MySQL-databasen kjører
    user="root",            # MySQL-brukernavn
    password="password",    # MySQL-passord
    database="bike_workshop"  # Navnet på databasen som skal kobles til
)

# Opprett en cursor for å utføre SQL-spørringer og hente resultater som ordbøker
cursor = db.cursor(dictionary=True)

# Definer ruten og funksjonen for søke-endepunktet
@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == "POST":  # Hvis forespørselen er POST (når brukeren sender inn skjemaet)
        product = request.form['product']  # Hent produktnavnet fra søkeskjemaet
        
        # SQL-spørring for å søke i Products-tabellen etter navn eller beskrivelse
        query = "SELECT name, description, price FROM Products WHERE name LIKE %s OR description LIKE %s"
        cursor.execute(query, (f"%{product}%", f"%{product}%"))  # Utfør spørringen med søketermene
        data = cursor.fetchall()  # Hent alle matchende poster

        # Hvis ingen resultater og brukeren har søkt på 'all', hent alle poster
        if len(data) == 0 and product.lower() == 'all': 
            cursor.execute("SELECT name, description, price FROM Products")
            data = cursor.fetchall()  # Hent alle produkter hvis 'all' ble søkt på

        return render_template('search.html', data=data)  # Render søkesiden med data
    
    return render_template('search.html')  # Render søkesiden ved GET-forespørsel (første last)

# Definer ruten og funksjonen for å legge til et nytt produkt
@app.route('/insert', methods=['GET', 'POST'])
def insert():
    if request.method == "POST":  # Hvis forespørselen er POST (når brukeren sender inn skjemaet)
        # Hent skjema-data for det nye produktet
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']

        # SQL-spørring for å sette inn det nye produktet i Products-tabellen
        query = "INSERT INTO Products (name, description, price) VALUES (%s, %s, %s)"
        cursor.execute(query, (name, description, price))  # Utfør spørringen med skjema-data
        db.commit()  # Bekreft transaksjonen til databasen

        # Viderekoble til søkesiden etter at produktet er lagt til
        return redirect(url_for('search'))

    return render_template('insert.html')  # Render innsettingssiden for GET-forespørsler

# Lukk databasen og cursor når appen stenges
@app.teardown_appcontext
def close_connection(exception):
    cursor.close()  # Lukk cursor
    db.close()  # Lukk databasen

# Kjør appen når skriptet kjøres
if __name__ == '__main__':
    app.debug = True  # Aktiver feilsøkingsmodus for enklere feilsøking under utvikling
    app.run()  # Start Flask-utviklingsserveren
