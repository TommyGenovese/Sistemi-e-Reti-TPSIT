from flask import Flask, render_template, redirect, url_for, request
import sqlite3, hashlib

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def validate():
    print("Validate")
    username = request.form['InputUsername']
    password = request.form['InputPassword']
    print(f"username: {username}, password: {password}")
    hashed_psw = hashlib.md5()
    hashed_psw.update(password.encode('utf-8'))
    hashed_psw = hashed_psw.hexdigest()
    print(f"hashed password: {hashed_psw}")

    #validazione password senza hash
    conn = sqlite3.connect("static/psw.db")
    cur= conn.cursor()
    cur.execute("SELECT * FROM users WHERE Username='" + username +"'")
    data = cur.fetchone()
    if data is None:
        return "This user does not exist"
    else:
        db_psw = cur.execute("SELECT * FROM users WHERE Username='" + username +"'")
        db_psw = db_psw.fetchall()
        print (f"{db_psw[0][1]}\n{hashed_psw}")
        if db_psw[0][1] == hashed_psw:
            return render_template('logged.html')
        else:
            return "Password incorrect"

    #validazione password con hash
    """
    with sqlite3.connect('static/psw.db') as conn:
        cur = conn.cursor()
        #seleziona il numero di utenti
        cur.execute("SELECT * FROM users")
        rows = cur.fetchall()
        for row in rows:
            #utente è nella prima colonna
            UserDB = row[0]
            #password è nella seconda colonna
            PassDB = row[1]
            
            #controllo 
            if UserDB == username:
                user_psw = hashlib.md5()
                user_psw.update(password.encode('utf-8'))
                user_psw = user_psw.hexdigest()
                completion = controlla_psw(PassDB, user_psw)
    return completion
    """


@app.route("/")             #http://127.0.0.1:6000/
def main():
    print("Main")
    return render_template("index.html")

@app.route("/login", methods=['GET','POST'])
def login():
    print("Login")
    return render_template('login.html')

if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)