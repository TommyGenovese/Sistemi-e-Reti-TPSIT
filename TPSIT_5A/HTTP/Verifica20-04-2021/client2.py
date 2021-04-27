import sqlite3
from flask import Flask, json,render_template, redirect, request, jsonify
from flask.helpers import url_for
import time, datetime
import requests
from flask import request

app = Flask(__name__)

def main():
    #richiedo i nomi di grandezza e stazione
    nome_grand = input("inserisci il nome della grandezza")
    nome_staz = input("inserisci il nome della stazione")
    #invio la richiesta get
    url = f"http://127.0.0.1:5000/valori?nome_grand={nome_grand}&id_staz={nome_staz}"
    r = requests.get(url)
    #prendo i 3 valori e li stampo a schermo
    minimo = json.loads(r.text)['valoreminimo']
    massimo = json.loads(r.text)['valoremassimo']
    media = json.loads(r.text)['valoremedio']
    
    print(f"nella stazione {nome_staz} i valori ottenuti per la {nome_grand} sono i seguenti:\n\tvalore minimo: {minimo}\n\tmedia: {media}\n\tvalore massimo: {massimo}")



if __name__ == "__main__":
    main()