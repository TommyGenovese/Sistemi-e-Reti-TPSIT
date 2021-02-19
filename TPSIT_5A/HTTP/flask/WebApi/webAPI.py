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

@app.route('/api', methods=['GET'])
def api_all():
    return jsonify(books)


if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=False)