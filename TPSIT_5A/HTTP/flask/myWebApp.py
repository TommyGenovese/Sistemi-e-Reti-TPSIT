from flask import Flask, render_template, redirect, url_for, request
import sqlite3, hashlib

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def validate():
    print("Validate")
    #lettura dati dal sito
    username = request.form['InputUsername']
    password = request.form['InputPassword']
    print(f"username: {username}, \npassword: {password}\n")
    #fase di hashing
    hashed_psw = hashlib.md5()
    hashed_psw.update(password.encode('utf-8'))
    hashed_psw = hashed_psw.hexdigest()
    print(f"hashed password: {hashed_psw}")

    conn = sqlite3.connect("static/psw.db")
    cur= conn.cursor()
    cur.execute("SELECT * FROM users WHERE Username='" + username +"'")
    data = cur.fetchone()
    if data is None:
        #error1 ="Not exists user"
        return "Warning❗, this user does not exists"
        #return render_template('login.html', error=error1)
    else:
        db_psw = cur.execute("SELECT * FROM users WHERE Username='" + username +"'")
        db_psw = db_psw.fetchall()
        print (f"{db_psw[0][1]}\n{hashed_psw}")
        if db_psw[0][1] == hashed_psw:
            return render_template('logged.html') ###
        else:
            error ="Invalid credentials"
        return render_template('login.html', error=error)


@app.route('/register', methods=['POST'])
def reg():
    print("SingUp")
    #lettura dati dal sito
    username = request.form['InputUsername']
    password = request.form['InputPassword']
    print(f"username: {username}, \npassword: {password}\n")
    #fase di hashing
    hashed_psw = hashlib.md5()
    hashed_psw.update(password.encode('utf-8'))
    hashed_psw = hashed_psw.hexdigest()
    print(f"hashed password: {hashed_psw}")

    conn = sqlite3.connect("static/psw.db")
    cur= conn.cursor()
    cur.execute("SELECT * FROM users WHERE Username='" + username +"'")
    data = cur.fetchone()
    if data is None:
        query="INSERT INTO users(Username, Password) VALUES ('"+username+"', '"+hashed_psw+"')"
        cur.execute(query)
        conn.commit()
        print(cur.rowcount, "record insert")
        return render_template('logged.html')
    else:
        error1 ="This user already exists"
    return render_template('register.html', error=error1)

@app.route("/")             #http://127.0.0.1:5000/
def main():
    print("Main")
    return render_template("index.html")

@app.route("/login", methods=['GET','POST'])
def login():
    print("Login")
    return render_template('login.html')

@app.route("/register", methods=['GET','POST'])
def register():
    print("Register")
    return render_template('register.html')

#delateble #Set the name of the person on the site view
@app.route("/logged", methods=['GET','POST'])
def logged():
    name = request.args.get("name")
    return render_template('logged.html', name=name)

if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=False)