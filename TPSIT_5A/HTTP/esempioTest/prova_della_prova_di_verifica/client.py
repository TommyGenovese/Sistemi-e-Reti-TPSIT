"""

    CLIENT di roba

"""


import sqlite3
from typing import Mapping
from flask import Flask, json,render_template, redirect, request, jsonify
from flask.helpers import url_for
import time
import requests
from flask import request

app = Flask(__name__)

def main():
    while True:
        #chiedo ip all'utente
        ip = input("IP>> ")
        url_get = f"http://127.0.0.1:5000/get_operation?ip={ip}"
        

        r = requests.get(url_get)   #invio la GET

        if r.status_code == 200:
            print(f"\tRICHIESTA INVIATA CORRETAMENTE\n\n{r.text}")


        #elaboro 

        #prendo l'oprezione e l'id
        operation = json.loads(r.text)['operation']    #da stringa simil dizionario a dizionario
        op_id = json.loads(r.text)['id']

        if operation == "CLOSE":
            break

        #calcolo l'operazione
        try:
            result = eval(operation)    #calcolo l'operaizone
            print(result)

        except ZeroDivisionError:   #se divide per zero invio come result un errore
            print("impossibile dividere per zero")
            result = "ZeroDivisionError"

        
        url_set = f"http://127.0.0.1:5000/set_result?id={op_id}&result={result}"
        r = requests.get(url_set)   #invio la GET

        if r.status_code == 200:
            print(f"\tRISULTATO INVIATO CORRETAMENTE\n\n")
        

        input("\nPress any key to send another request...")


if __name__ == "__main__":
    main()