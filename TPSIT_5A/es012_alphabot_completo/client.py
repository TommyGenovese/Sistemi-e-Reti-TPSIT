"""

Author: Genovese Tommaso
Date: 23-03-2021

Client alphabot

"""

import sqlite3
from sqlite3.dbapi2 import connect
from flask import Flask,render_template, redirect, request, jsonify
from flask.helpers import url_for
import time
import requests
import json
import Alphabot
from threading import Thread

class controllerSensori (Thread):
    def __init__(self, pinSX, pinDX):   #passo i pin dei sensori
        Thread.__init__(self)
        self.pinSX = pinSX
        self.pinDX = pinDX

        #stato dei sensori
        self.precDX = 0
        self.precSX = 0
        self.currDX = 0
        self.currSX = 0

        #setting dei sensori
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.pinDX,GPIO.IN,GPIO.PUD_UP)
        GPIO.setup(self.pinSX,GPIO.IN,GPIO.PUD_UP)

    def run(self):
        #leggo lo stato attuale dei sensori
        self.currDX = GPIO.input(self.pinDX)   #0 - 1
        self.currSX = GPIO.input(self.pinSX)

        while True:
            #controllo se ci sono stati dei cambiamenti
            if self.currDX != self.precDX or self.currSX != self.precSX:
                if not self.currDX and not self.currSX:
                    statoOstacolo = "SCOMPARSO"
                elif self.currSX and not self.currDX:
                    statoOstacolo = "SINISTRA"
                elif not self.currSX and self.currDX:
                    statoOstacolo = "DESTRA"
                elif self.currSX and self.currDX:
                    statoOstacolo = "CENTRO"
                
                #invio lo stato aggiornato dell'ostacolo
                request.get(f"http://192.168.1.124:5000/ostacoli?status={statoOstacolo}") 
            
            #aggiorno lo stato attuale dei sensori
            self.precSX = self.currSX
            self.precDX = self.currDX     

            time.sleep(500) #ripeto ogni 500 ms

def main():
    inizio = input("INIZIO >> ")
    fine = input("FINE   >> ")

    url = f"http://192.168.1.124:5000/percorsi?start={inizio}&end={fine}"

    r = requests.get(url)   #invio la get
    if r.status_code == 200:    #tutto OK
        print("richiesta riuscita")

    #leggo i percorsi possibili dalla API
    paths = []
    for d in json.loads(r.text):    #trasformo la stringa in un dizionario
        paths.append(d['path'])

    print(paths)

    bot = alphabot.Alphabot()
    bot.stop()

    #avvio un thread per la lettura dei sensori
    listener = controllerSensori(19,16)
    listener.start()

    #parsing del path
    print("parsing")
    for path in paths: 
        index = 0
        
        while index < len(path):
            distance = ''
            if path[index] == 'W':
                index = index + 1
                while index < len(path) and path[index].isnumeric():
                    distance = distance + path[index]
                    index = index + 1
                bot.forward()
                time.sleep(int(distance))
                bot.stop()
                print("avanti"+distance)

            elif path[index] == 'S':
                index = index + 1
                while index < len(path) and path[index].isnumeric():
                    distance = distance + path[index]
                    index = index + 1
                bot.backward()
                time.sleep(int(distance))
                bot.stop()

            elif path[index] == 'A':
                index = index + 1
                while index < len(path) and path[index].isnumeric():
                    distance = distance + path[index]
                    index = index + 1
                bot.left()
                time.sleep(int(distance))
                bot.stop()

            elif path[index] == 'D':
                index = index + 1
                while index < len(path) and path[index].isnumeric():
                    distance = distance + path[index]
                    index = index + 1
                bot.right()
                time.sleep(int(distance))
                bot.stop()

if __name__ == "__main__":
    main()
