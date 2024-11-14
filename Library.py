from flask import Flask, jsonify, request, render_template, redirect, url_for
import mysql.connector

app = Flask(__name__,
            static_url_path='', 
            static_folder='Static',
            template_folder='Templates')

# MySQL database connection 
db = mysql.connector.connect(
    host="localhost",       
    user="root",            
    password="password",    
    database="bike_workshop"
)
cursor = db.cursor(dictionary=True)

# Endpoint for search
@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        product = request.form['product']
        # Search by product name or description
        query = "SELECT name, description, price FROM Products WHERE name LIKE %s OR description LIKE %s"
        cursor.execute(query, (f"%{product}%", f"%{product}%"))
        data = cursor.fetchall()

        # If "all" is in the search box, retrieve all records
        if len(data) == 0 and product.lower() == 'all': 
            cursor.execute("SELECT name, description, price FROM Products")
            data = cursor.fetchall()

        return render_template('search.html', data=data)
    
    return render_template('search.html')

# Endpoint for inserting a new product
@app.route('/insert', methods=['GET', 'POST'])
def insert():
    if request.method == "POST":
        # Retrieve form data
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']

        # Insert the new product into the Products table
        query = "INSERT INTO Products (name, description, price) VALUES (%s, %s, %s)"
        cursor.execute(query, (name, description, price))
        db.commit()

        # Redirect to search page after inserting
        return redirect(url_for('search'))

    return render_template('insert.html')

# Close the cursor and connection when the app shuts down
@app.teardown_appcontext
def close_connection(exception):
    cursor.close()
    db.close()

if __name__ == '__main__':
    app.debug = True
    app.run()
