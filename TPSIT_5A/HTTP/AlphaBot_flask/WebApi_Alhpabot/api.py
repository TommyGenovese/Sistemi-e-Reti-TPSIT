from flask import Flask, render_template, redirect, url_for, request, jsonify
import json, sqlite3

app = Flask(__name__)

@app.route('/api/percorsi', methods=['GET'])
def api_percorsi():
    print(f"\n{request.args}\n")
    if 'partenza' in request.args:
        partenza = request.args['partenza']
    else:
        return "Error: No path field provided. Please specify a path"
    
    if 'arrivo' in request.args:
        end = request.args['arrivo']
    else:
        return "Error: No end field provided. Please specify an end"
    
    conn = sqlite3.connect("static/path.db")
    cur= conn.cursor()
    cur.execute(f"SELECT if.id_start FROM inizio_fine if")
    
    cur.execute(f"SELECT if.id_start AS id_partenza, if.id_end AS id_arrivo FROM inizio_fine if, percorsii p, luoghi l WHERE p.id = if.id_percorso AND (if.id_start = {partenza} OR if.id_end = {end})")
    data = cur.fetchall()
    print(data)
    conn.close()
    return jsonify(data)

@app.route('/', methods=['GET'])
def home():
    return "<h1>Web API flask</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404 Page not found</h1><p>Write better your code idiot!</p>"

if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)