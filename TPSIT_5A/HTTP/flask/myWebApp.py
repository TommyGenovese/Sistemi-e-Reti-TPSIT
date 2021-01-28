from flask import Flask, render_template, redirect, url_for, request
import sqlite3, hashlib

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def validate():
    print("Validate")
    username = "nomeProva" #request.form['InputUsername']
    password = "PasswordProva" #request.form['InputPassword']
    #validazione password
    cur = sqlite3.connect("psw.db")
    cur.execute("SELECT * FROM users WHERE Username='" + username + "' AND Password ='" + password + "'")
    data = cur.fetchone()
    if data is None:
        return "username or Password is wrong"
    else:
        return "logged in successfully"


@app.route("/")             #http://127.0.0.1:5000/
def main():
    print("Main")
    return render_template("index.html")

@app.route("/login", methods=['GET','POST'])
def login():
    print("Login")
    #validate()
    return render_template('login.html')


if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)