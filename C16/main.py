from flask import Flask, render_template, redirect, Blueprint, request, url_for, flash, session
import os
from dotenv import load_dotenv
import hashlib

print("Username is 'SuperUser'")
print("Password is 'SuperUser123'")

app = Flask(__name__)
auth_bp = Blueprint('auth', __name__)
app.secret_key = "blahblahblah"

load_dotenv()

@app.route('/')
def index():
    return render_template('index.html', name=session.get('name', 'Guest'))

@auth_bp.route('/login',methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usernameinput = request.form['username']
        passwordinput = request.form['password']

        username = os.getenv('USERNAME')
        password = os.getenv('HASHED_PASSWORD')

        salt ="salty"
        saltedinput = salt + passwordinput
        inputhash = hashlib.sha256(saltedinput.encode('utf-8')).hexdigest()

        if usernameinput == username and inputhash == password:
            session['name'] = username
            return redirect(url_for('index'))
        
        flash('Invalid username or password')

    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))
  
if __name__ == '__main__':
    app.register_blueprint(auth_bp)
    app.run(debug=True)
    