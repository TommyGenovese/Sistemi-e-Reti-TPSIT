import sqlite3
import socket
IpAddress = 'localhost'
port = 5004

srv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

srv.bind((IpAddress,port))

while(True):

    #ricezione del messaggio
    data, address = srv.recvfrom(4096)
    end_start = str(data, 'UTF8').split(',')
    print(f"msg from client: {data}") #{end_start[0]}, {end_start[1]}")
    sent = srv.sendto(data, address)
    #print (f"sent {data.encode()} bytes back to {IpAddress}")

    srv.sendto(str(data).encode(), address) 

srv.close()