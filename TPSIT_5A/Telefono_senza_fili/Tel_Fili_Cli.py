import socket

IpAddress = 'localhost'
port = 5004

cli = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while(True):
    #invio del messaggio
    msg = input("testo del messaggio:")
    cli.sendto(msg.encode(),(IpAddress,port))

    #ricezione messaggio di conferma
    data = cli.recv(8036)
    print(data)

cli.close()