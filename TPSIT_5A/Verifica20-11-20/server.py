import socket
import threading
import sys
import sqlite3
import os

IpAddress = 'localhost'
port = 5004
db_name = "operations.db"
client = {}
thread = []

class ClietThread(threading.Thread):
    def __init__(self,ip,port,connection): 
        #creo il costruttore con le varie variabili
        threading.Thread.__init__(self)
        self.ip_address = ip
        self.port = port
        self.connection = connection
        self.again = 1

    def run(self):  
        #codice che esegue il thread
        while self.again:
            with sqlite3.connect(db_name) as data_base:
                self.cursor = data_base.cursor()
                #eseguire la query

                if(num_cli == 1):
                    #procedere per il primo client

                    #ciclo per il numero di record presenti nel database
                    for id_db in self.cursor.execute("SELECT count(*) FROM operations"):
                        #verifico che il numero del client(1) sia lo stesso del client nel database
                        cliente = self.cursor.execute("SELECT client FROM operations WHERE id = "+id_db)
                        if(num_cli == cliente):
                            #prendo dal db l'operazione che dovrà svolgere il client e la metto in query
                            query = self.cursor.execute("SELECT operation FROM operations WHERE id = "+id_db)
                            conn.sendto(query, addr)
                            ris = conn.recv()
                            print(f"{query} = {ris} from {addr}") 

                    #tabella esaurita, invio dell'exit
                    exit = "exit"
                    self.again = 0
                    conn.send(exit.encode())
                    Stop_connessione(self)
                    
                else:
                    #procedere per il secondo client
                    #ciclo per il numero di record presenti nel database
                    for id_db in self.cursor.execute("SELECT count(*) FROM operations"):
                        #verifico che il numero del client(2) sia lo stesso del client nel database
                        cliente = self.cursor.execute("SELECT client FROM operations WHERE id = "+id_db)
                        if(num_cli == cliente):
                            #prendo dal db l'operazione che dovrà svolgere il client e la metto in query
                            query = self.cursor.execute("SELECT operation FROM operations WHERE id = "+id_db)
                            conn.sendto(query, addr)
                            ris = conn.recv()
                            print(f"{query} = {ris} from {addr}")
                            
                    #tabella esaurita, invio dell'exit
                    exit = "exit"
                    self.again = 0
                    conn.send(exit.encode())
                    Stop_connessione(self)
                    

def Stop_connessione(t):
    global thread
    thread.pop(thread.index(t))

                    
def main():
    global num_cli
    global conn
    global addr
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    num_cli = 0

    srv.listen()

    while True:
        #new connection
        print("in attesa di connessione...")
        conn, addr = srv.accept()

        print(f"client {num_cli} connesso")
        num_cli += 1
        client[num_cli] = addr

        #creo il thread e lo faccio partire
        t = ClietThread(addr[0],addr[1],conn)
        t.start()

        #updating tables
        thread.append(t)

if __name__ == "__main__":
    main() 