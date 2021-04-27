import sqlite3
from sqlite3.dbapi2 import Cursor
from os import stat
from flask import Flask, json,render_template, redirect, request, jsonify
from flask.helpers import url_for
import time
import requests
from flask import request

app = Flask(__name__)

@app.route('/id_grandezza')
def grandezza():
    #chiedo il nome della grandezza all'utente
    name_grand= request.args['name']

    #mi connetto al db per ottenere l'id della grandezza
    with sqlite3.connect("meteo.db") as conn:
        cur = conn.cursor()
        query= f"SELECT id_misura FROM grandezze WHERE grandezza_misurata = '{name_grand}'"
        cur.execute(query)
        id_grandezza = cur.fetchone() #prendo solo il primo dato
        print(id_grandezza)

        return(jsonify({'id' : id_grandezza[0]}))


@app.route('/id_staz')
def stazione():
    #chiedo il nome della grandezza all'utente
    name_staz= request.args['name']

    with sqlite3.connect("meteo.db") as conn:
        cur = conn.cursor()
        cur.execute(f"SELECT id_stazione FROM stazioni WHERE nome = '{name_staz}'")
        id_stazione = cur.fetchone() #prendo solo il primo dato
        print(id_stazione)

        return(jsonify({'id' : id_stazione[0]}))


@app.route('/imposta_misura')
def imp_misura():
    #estrapolo i 4 dati
    misura = request.args["misura"]
    id_grand = request.args["id_grand"]
    id_staz = request.args["id_staz"]
    quando = request.args["quando"]
    print(f"valori inseriti alla stazione {id_staz}, grandezza: {id_grand}, valore della misura: {misura}, nel giorno: {quando}")

    with sqlite3.connect("meteo.db") as conn:
        cur = conn.cursor()
        #essendo id_misurazione autoincrement posso evitare di inserirlo nella query
        cur.execute(f"INSERT into misurazioni(id_stazione, id_grandezza, data_ora, valore) values({id_staz},{id_grand},{quando},{misura})")

        return(jsonify({'state' : 'Inserimento riuscito'}))

@app.route('/valori')   
def valori():
    #ottengo i valori dai parametri
    nome_grand = request.args["nome_grand"]
    nome_staz = request.args["nome_staz"]

    #mi connetto al db per convertire i nomi in id
    with sqlite3.connect("meteo.db") as conn:
        cur = conn.cursor()
        #seleziono l'iddove il nome corriponde
        cur.execute(f"SELECT id_stazione from stazioni WHERE nome = {nome_staz}")
        id_staz=cur.fetchone()
        cur2 = conn.cursor()
        #seleziono l'id dove la grandezza corrisponde
        cur2.execute(f"SELECT id_misura from grandezze WHERE grandezza_misurata = {nome_grand}")
        id_grand=cur2.fetchone()

    print(f"grandezza inserita: {id_grand}, stazione inserita: {id_staz}")

    #mi connetto una seconda volta per calcolare i 3 valori e successivamente li restituisco con il return
    with sqlite3.connect("meteo.db") as conn:
        cur = conn.cursor()
        #ottendo il minimo, il massimo e la media
        cur.execute(f"SELECT MIN(valore), MAX(valore), AVG(valore) FROM misurazioni WHERE id_grandezza = {id_grand} AND id_stazione = {id_staz}")
        stats = cur.fetchone()
        return(jsonify({'valoreminimo' : stats[0],
                        'valoremedio' : stats[2],
                        'valoremassimo' : stats[1]}))


if __name__ == "__main__":
    app.run(host="127.0.0.1", debug = True)
