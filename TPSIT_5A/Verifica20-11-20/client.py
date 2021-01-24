import socket
IpAddress = 'localhost'
port = 6000
#STREAM dato che è tcp e conncetion per connettersi al server con porta e IP prec. specificati
cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cli.connect((IpAddress, port))

while(True):
    #ricezione del messaggio con l'operazione e stampa
    oper = cli.recv(4096)
    oper = oper.decode()
    #interruzione in caso di exit
    if str(oper) == "exit":
        break
    ris = eval(oper)
    print(ris)
    ris = str(ris)
    #invio del risultato
    ris = ris.encode()
    cli.send(ris)
cli.close()