"""

    SERVER 

"""


import sqlite3
from sqlite3.dbapi2 import Cursor
from typing import Mapping
from flask import Flask, json,render_template, redirect, request, jsonify
from flask.helpers import url_for
import time
import requests
from flask import request

app = Flask(__name__)

@app.route('/get_operation')
def get_an_operation():
    #prendo l'ip dall'URL
    ip = request.args["ip"]

    #controllo se l'ip e' nella whitelist
    with sqlite3.connect("static/operations.db") as conn:
        cursor = conn.cursor()

        cursor.execute(f"SELECT ip FROM ip_consentiti WHERE ip = '{ip}'")
        allowed = cursor.fetchall()

        

        if allowed:
            #all'ip e' concesso ricevere
            cursor.execute(f"SELECT id, operazione FROM operazioni WHERE calcolata = 0")
            query_result = cursor.fetchone()

            print(query_result)

            if query_result == None:
                return(jsonify({"id" : -1, "operation" : "CLOSE"}))

            ide = query_result[0]
            operation = query_result[1]

            

            cursor.execute(f"UPDATE operazioni SET inviata = 1 WHERE id = {ide}")
            cursor.fetchone()

            print(f"""
            
                SENDING:        {ide} : {operation}
                DESTINATION:    {ip}   

            """)

            return(jsonify({'id' : ide, 'operation' : operation}))

        else:
            print("noNNNNNNNNNN esiste")

@app.route('/set_result')
def set_a_result():
    #prendo id e risultato dall'URL
    op_id = request.args["id"]
    result = request.args["result"]

    print(f"""
    
    id:     {op_id}
    result: {result}
    
    """)

    with sqlite3.connect("static/operations.db") as conn:
        cursor = conn.cursor()

        #cambio lo stato dell'operazione e mettere calcolata a 1
        cursor.execute(f"UPDATE operazioni SET calcolata = 1 WHERE id = {op_id}")
        cursor.fetchone()

        #inserisco il risultato
        cursor.execute(f"INSERT INTO risultati (id, risultato) VALUES ({op_id},'{result}')")
        cursor.fetchone()




    return " RISULTATI INSERITI CORRETTAMENTE "

if __name__ == "__main__":
    app.run(host="127.0.0.1", debug = True)