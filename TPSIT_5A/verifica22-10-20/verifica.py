import socket
import time
IpAddress = 'localhost'
port = 1024 #dal 1024 iniziano le porte utilizzabili
MAX_PORT = 40000

cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while port< MAX_PORT:
    #richiesta di connessione da parte del client al server
    if(cli.connect_ex((IpAddress, port))==0):
        print(f"connessione effettuata alla porta: {port} "+ str(cli.connect_ex((IpAddress, port))))
    else:
        print(f"connessione fallita alla porta: {port} "+ str(cli.connect_ex((IpAddress, port))))

    port = port + 1
    #time.sleep(0.1)
    cli.close()