from flask import Flask, render_template, redirect, url_for, request
import sqlite3, hashlib, semaforo, datetime
#add log
app = Flask(__name__)

#collegarsi a questo indirizzo: 127.0.0.1:5000/


s = semaforo.semaforo()
NewStato = "OFF"
PrevStato = "ON"
@app.route('/', methods=['POST'])
def setting():
    global PrevStato
    DurVer = request.form['DurVer']
    DurGia = request.form['DurGia']
    DurRos = request.form['DurRos']
    NewStato = request.form['stato']
    today = datetime.datetime.now()
    #controllo se il semaforo è impostato su ON, OFF o niente
    if NewStato == "ON":
        #Se lo stato non cambia NON segno nel database
        if NewStato == PrevStato:
            s.rosso(int(DurRos))
            s.verde(int(DurVer))
            s.giallo(int(DurGia))
            #se prova a togliere la riga successiva il codice funziona, mi dà l'errore di non aver dato un valore ma è assegnato all'inizio del programma
            PrevStato=NewStato
            return "semaforo aggiornato: \n\tverde="+DurVer+"\n\tgiallo="+DurGia+"\n\trosso="+DurRos 
        #Se lo stato cambia segno nel database
        else:
            conn = sqlite3.connect("static/database.db")
            cur= conn.cursor()
            query="INSERT INTO registro(data, oper) VALUES ('"+str(today)+"', 'ON')"
            cur.execute(query)
            conn.commit()
            conn.close()
            s.rosso(int(DurRos))
            s.verde(int(DurVer))
            s.giallo(int(DurGia))
            #se prova a togliere la riga successiva il codice funziona, mi dà l'errore di non aver dato un valore ma è assegnato all'inizio del programma
            PrevStato=NewStato
            return "semaforo acceso ed aggiornato: \n\tverde="+DurVer+"\n\tgiallo="+DurGia+"\n\trosso="+DurRos
        

        #medesima cosa di sopra
    elif NewStato =="OFF":
        if NewStato != PrevStato:
            conn = sqlite3.connect("static/database.db")
            cur= conn.cursor()
            query2="INSERT INTO registro(data,  oper) VALUES ('"+str(today)+"', 'OFF')"
            cur.execute(query2)
            conn.commit()
            conn.close()
        for _ in range(3):
            s.giallo(1)
            s.luci_spente(1)
        #se prova a togliere la riga successiva il codice funziona, mi dà l'errore di non aver dato un valore ma è assegnato all'inizio del programma
        PrevStato=NewStato
        return "semaforo aggiornato e spento"
    
    #se non si imposta nessuno stato del semaforo
    else:
        if PrevStato == "ON":
            s.rosso(int(DurRos))
            s.verde(int(DurVer))
            s.giallo(int(DurGia))
            return "impostazioni effettuate"
        else:
            return "Al momento il semaforo è spento"



@app.route("/")             #http://127.0.0.1:5000/
def main():
    print("Main")
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=False)