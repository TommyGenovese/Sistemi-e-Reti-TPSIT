import sqlite3
from flask import Flask, json,render_template, redirect, request, jsonify
from flask.helpers import url_for
import time, datetime
import requests
from flask import request

app = Flask(__name__)

def main():
    while True:
        #faccio inserire la grandezza all'utente
        name_gra = input("inserire la grandezza: ")
        url_get = f"http://127.0.0.1:5000/id_grandezza?name={name_gra}"
        r = requests.get(url_get)  
        #questo comando rende una stringa un dizionario
        id_grand = json.loads(r.text)['id']
        print("L'ID della grandezza è: "+id_grand)

        #Faccio inserire il nome della stazione all'utente
        name_st = input("inserire la stazione: ")
        url_get = f"http://127.0.0.1:5000/id_stazione?name={name_st}"
        r = requests.get(url_get)
        id_staz=json.loads(r.text)['id']
        print("L'ID della stazione è :"+id_staz)

        #Faccio inserire le misure dall'utente
        misura = input("inserisci la misura da registrare: ")
        url = f"http://127.0.0.1:5000/imposta_misura?misura={misura}&id_grand={id_grand}&id_staz={id_staz}&quando={datetime.datetime.now()}"
        r = requests.get(url)   #invio la GET

        #controllo che l'operazione sia stata eseguita correttamente (200 = nessun errore)
        if r.status_code == 200:
            print("misurazione inserita nel database")
        else:
            print("errore durante l'inserimento del valore")


if __name__ == "__main__":
    main()
