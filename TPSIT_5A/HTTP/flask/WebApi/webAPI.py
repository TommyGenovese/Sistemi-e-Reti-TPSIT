from flask import Flask, render_template, redirect, url_for, request, jsonify
import json, sqlite3

app = Flask(__name__)

@app.route('/api/books/all', methods=['GET'])
def api_all():
    conn = sqlite3.connect("database.db")
    cur= conn.cursor()
    cur.execute("SELECT * FROM libri")
    data = cur.fetchall()
    print(data)
    conn.close()
    return jsonify(data)

@app.route('/api/books', methods=['GET'])
def api_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id"
    
    conn = sqlite3.connect("database.db")
    cur= conn.cursor()
    cur.execute(f"SELECT * FROM libri WHERE id={id}")
    dataID = cur.fetchall()
    print(dataID)
    conn.close()
    
    return jsonify(dataID)

@app.route('/api/books/title', methods=['GET'])
def api_title():
    print(f"\n{request.args}\n")
    if 'title' in request.args:
        title = request.args['title']
    else:
        return "Error: No title field provided. Please specify an title"
    
    conn = sqlite3.connect("database.db")
    cur= conn.cursor()
    cur.execute(f"SELECT * FROM libri WHERE titolo='{title}'")
    dataTIT = cur.fetchall()
    print(dataTIT)
    conn.close()
    
    return jsonify(dataTIT)

@app.route('/api/books/author', methods=['GET'])
def api_author():
    print(f"\n{request.args}\n")
    if 'author' in request.args:
        author = request.args['author']
    else:
        return "Error: No author field provided. Please specify an author"
    
    conn = sqlite3.connect("database.db")
    cur= conn.cursor()
    cur.execute(f"SELECT * FROM libri WHERE author='{author}'")
    dataAUT = cur.fetchall()
    print(dataAUT)
    conn.close()
    
    return jsonify(dataAUT)

@app.route('/', methods=['GET'])
def home():
    return "<h1>Web API flask</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404 Page not found</h1><p>Write better your code idiot!</p>"

if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)