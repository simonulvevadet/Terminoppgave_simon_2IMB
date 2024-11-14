from flask import Flask, jsonify, request, render_template
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
cursor = db.cursor(dictionary=True)  # Enable dictionary mode to get results as dictionaries

# Endpoint for search
@app.route('/search', methods=['GET', 'POST'])
def search():
    data = None  # Initialize data variable
    if request.method == "POST":
        search_query = request.form.get('search_query')  # Retrieve the search query from the form
        
        # Search by product name or description
        query = "SELECT name, description FROM Products WHERE name LIKE %s OR description LIKE %s"
        cursor.execute(query, (f"%{search_query}%", f"%{search_query}%"))
        data = cursor.fetchall()
        
        # If no results and 'all' is entered, return all products
        if len(data) == 0 and search_query.lower() == 'all': 
            cursor.execute("SELECT name, description FROM Products")
            data = cursor.fetchall()
    
    # Render the search template with the results (or none if no search has been made yet)
    return render_template('search.html', data=data)

if __name__ == '__main__':
    app.debug = True
    app.run()
