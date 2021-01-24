from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")             #http://127.0.0.1:6000/
def index():
    return render_template("palestra.html")



if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)