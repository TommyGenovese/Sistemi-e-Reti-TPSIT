import socket
Ip_address= "localhost"
port = 1024

while(True):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    s.bind((Ip_address,port))
    print("ricezione:")
    s.listen()
    c,address = s.accept()

    s.close()
    port= port+1