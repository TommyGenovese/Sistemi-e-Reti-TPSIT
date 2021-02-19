from flask import Flask, render_template, redirect, url_for, request, jsonify
import json

app = Flask(__name__)


books=[
    {
    'id':0,
    'title': 'Il nome della Rosa',
    'author': 'Umberto Eco'
    },
    {
    'id': 1,
    'title': 'Il problema dei tre corpi',
    'author': 'Liu Cixin'
    },
    {
    'id':2,
    'title': 'Fondazione',
    'author': 'Isacc Asimov'
    }
]

@app.route('/api/books/all', methods=['GET'])
def api_all():
    return jsonify(books)

@app.route('/api/books', methods=['GET'])
def api_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id"
    
    results = []

    for book in books:
        if book['id'] == id:
            results.append(book)
    
    return jsonify(results)

@app.route('/api/books/title', methods=['GET'])
def api_title():
    if 'title' in request.args:
        title = request.args['title']
    else:
        return "Error: No title field provided. Please specify an title"
    
    results = []

    for book in books:
        if book['title'] == title:
            results.append(book)
    
    return jsonify(results)

@app.route('/', methods=['GET'])
def home():
    return "<h1>Web API flask</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404 Page not found</h1><p>Write better your code idiot!</p>"

if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)