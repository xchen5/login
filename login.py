from flask import Flask, render_template, request, session, redirect
import os

my_app = Flask(__name__)

my_app.secret_key = os.urandom(32)

login_dict = {}

@my_app.route('/', methods = ['GET','POST'])
def root():
    if bool(session) != False:
        return render_template("welcome.html", username = session['user'])
    else:
        return render_template('login_form.html')


@my_app.route('/welcome/', methods = ['GET','POST'])
def welcome():
    user = request.form['user']
    password = request.form['password']
    if request.form['submit'] == "Sign Up":
        if (user in login_dict):
            return render_template('error.html', error = "Username Taken")
        login_dict[user] = password
        session['user'] = user
        session['pass'] = password
        return render_template('welcome.html', username = user)
    if request.form['submit'] == "Log In":
        if not (user in login_dict):
            return render_template ('error.html', error = "Username not Found")
        if password != login_dict[user]:
            return render_template('error.html', error = "Incorrect Password")
        if password == login_dict[user]:
            return render_template('welcome.html', username = user)

@my_app.route('/logout/', methods= ['GET', 'POST'])
def logout():
    session.pop('user')
    session.pop('pass')
    return render_template('login_form.html')
if __name__ == '__main__':
    my_app.debug = True
    my_app.run()
