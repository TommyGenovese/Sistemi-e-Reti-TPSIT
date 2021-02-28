import semaforo
from flask import Flask
import time

app = Flask(__name__)

s = semaforo.semaforo()
STATO = "SPENTO" #"SPENTO"

#ESEMPIO di pagina di test
@app.route('/test')
def test():
    if STATO == "ATTIVO":
        #Esempio di sequenza con semaforo attivo. I tempi devono essere
        #modificabili dalla pagina di configurazione!
        s.rosso(2)
        s.verde(2)
        s.giallo(1)
    else:
        #Esempio di sequenza con semaforo spento. I tempi devono essere
        #modificabili dalla pagina di configurazione!
        for _ in range(3):
            s.giallo(1)
            s.luci_spente(1)
    return 'TEST ESEGUITO!'


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
