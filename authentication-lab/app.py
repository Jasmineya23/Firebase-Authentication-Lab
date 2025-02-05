from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase
 confing={
    "apiKey": "AIzaSyB5zG8KLY9EHMHfuwJ1lyjwsE8EQtJ-lzE",
    "authDomain": "group-e-983a2.firebaseapp.com",
    "projectId": "group-e-983a2",
    "storageBucket": "group-e-983a2.appspot.com",
    "messagingSenderId": "608015798420",
    "appId": "1:608015798420:web:84208baf5454e826a9e481",
    "measurementId": "G-PV5NV5P3EN"
    "databaseURL":""
    }
    firebase = pyrebase.ini

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    return render_template("signin.html")
    error = ""
   if request.method == 'POST':
       email = request.form['email']
       password = request.form['password']
       try:
            login_session['user'] = 
auth.sign_in_with_email_and_password(email, password)
           return redirect(url_for('home'))
       except:
           error = "Authentication failed"
   return render_template("signin.html")



@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = ""
    if request.method == 'POST':
       email = request.form['email']
       password = request.form['password']
       try:
            login_session['user'] = 
auth.create_user_with_email_and_password(email, password)
           return redirect(url_for('home'))
       except:
           error = "Authentication failed"
   return render_template("signup.html")
    return render_template("signup.html")

    @app.route('/signout')
def signout():
    login_session['user'] = None
auth.current_user = None
return redirect(url_for('signin'))


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")


if __name__ == '__main__':
    app.run(debug=True)