#app.py
from flask import Flask, request, session, redirect, url_for, render_template, flash
import psycopg2 #pip install psycopg2 
import psycopg2.extras
 
app = Flask(__name__)
app.secret_key = 'flask'
 
DB_HOST = "login-back"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = "password"
 
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)

@app.route('/login/', methods=['GET', 'POST'])
def login():
    
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
   
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
 
        # Check if account exists using MySQL
        cursor.execute('SELECT * FROM public.users WHERE username = %s', (username,))
        # Fetch one record and return result
        account = cursor.fetchone()
 
        if account:
            # If account exists in users table in out database
            if account['username'] == username and account['password'] == password:
                flash('Correct username/password')
            else:
                # Account doesnt exist or username/password incorrect
                flash('Incorrect password')
        else:
            # Account doesnt exist or username/password incorrect
            flash('Account does not exist')
 
    return render_template('login.html')
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)
