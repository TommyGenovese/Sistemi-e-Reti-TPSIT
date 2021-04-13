"""

    SERVER ALPHABOT

"""


import sqlite3
from typing import Mapping
from flask import Flask, json,render_template, redirect, request, jsonify
from flask.helpers import url_for
import time
import requests
from flask import request

app = Flask(__name__)

#mapping dello stato dei sensori VALORE : [sensoreSX, sensoreDX]
obstaclesMapping = {
    "SCOMPARSO" : [0,0],
    "SINISTRA" : [1,0],
    "DESTRA" : [0,1],
    "CENTRO" : [1,1]
}

@app.route("/percorsi", methods = ['GET'])
def get_path():
    """

    API che, dato un'inizio e una fina dell'URL della GET, 
    interroga il DB sui percorsi e ritorna al clienti i 
    percorsi percorribili.

    """

    #prendo il luogo di inizio e il luogo di fine dall'URL
    start = request.args["start"]
    end = request.args["end"]

    print(f"{start}\n{end}")

    if request.method == "GET":
        #connessione al db dei percorsi
        with sqlite3.connect("D:\GitHub\AlphaBot\es012_alphabot_completo\static\percorsi.db") as conn:
            cursor = conn.cursor()

            #selezioni gli id dei luoghi passati nell'URL
            cursor.execute(f"SELECT id FROM luoghi WHERE luoghi.nome = '{start}' OR  luoghi.nome = '{end}' ")
            ids = list(cursor.fetchall())

            print(ids)

            #sleziono i percorsi possibili
            cursor.execute(f"SELECT percorso FROM percorsi, inzio_fine WHERE inzio_fine.id_start = {int(ids[0][0])} AND inzio_fine.id_end = {int(ids[1][0])} AND percorsi.id = inzio_fine.id_percorso ")
            percorsi = cursor.fetchall()
            
            #inserisco i percorsi possibili in un dizionario, che a sua volta e' inserito in una lista
            paths = []
            for percorso in percorsi[0]:
                paths.append({"id" : percorsi[0].index(percorso), "path" : percorso})
                print(paths)

            return jsonify(paths)


@app.route("/ostacoli", methods = ['GET'])
def obstacles():
    """
    
    API che, ricevuto lo stato di un ostacolo, ricava la lettura dei singoli
    sensori e inserisce i dati nel db dedicato

    """

    global obstaclesMapping #mapping dello stato dei sensori

    #leggo lo stato dall'URL
    stato = request.args["status"]
    print(stato)
    #connessione al db degli ostacoli
    with sqlite3.connect("static/ostacoli.db") as conn:
        cursor = conn.cursor()

        cursor.execute(f"INSERTO INTO ostacoli (stato, sensoreSX, sensoreDX) values ('{stato}',{obstaclesMapping[stato][0]},{obstaclesMapping[stato][1]})")  
        cursor.fetchall()

    #returno una pagina web con i dati inseriti nel DB
    return f"""

    DATI INSERITI:

        stato = {stato}
        sensoreSX = {obstaclesMapping[stato][0]}
        sensoreDX = {obstaclesMapping[stato][1]}

    """

if __name__ == "__main__":
    app.run(host="192.168.0.121", debug = True)

