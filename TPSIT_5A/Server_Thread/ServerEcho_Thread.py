import threading as thread
import socket


host= "localhost"
port= 6006
listaThread=[]

srv=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv.bind((host,port))

class clientThread(thread.Thread):

    def __init__(self , ip, port, conn):
        thread.Thread.__init__(self)
        self.ip_address = ip
        self.port = port
        self.conn = conn
        self.again = 1
        print(f"nuovo thread {ip}, {port}")
    
    def run(self):
        print(f"connessione da {ip}, {port}")

        while True:
            data= cli.recv(4086)
            data = data.decode()
            print(f"messaggio ricevuto:  {data}")
            data = data.encode()
            cli.send(data)
        print("Client disconnesso...")
        cli.close()


while (True):
    srv.listen()
    print("Listen...")
    cli, (ip, port) = srv.accept()
    t=clientThread(ip, port, cli)
    t.start()
    listaThread.append(t)

for t in threads:
    t.join()