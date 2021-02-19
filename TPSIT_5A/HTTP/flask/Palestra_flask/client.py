import socket
IpAddress = '127.0.0.1'
port = 5000
url ="http://"
cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cli.connect((IpAddress, port))
done = False
#while not done:
password="ciaociao"
body = "InputUsername=Tommy&InputPassword=ciaociao"
bodylen= str(len(body))
richiesta = f"POST http://127.0.0.1:5000/login HTTP/1.1\nHost: 127.0.0.1:5000\nConnection: keep-alive\nContent_Type: application/x-www-form-urlencoded\nContent_Lenght: {len(body)}\n\n{body}"
print(richiesta)
cli.sendall(richiesta.encode())

#if done: #if i'm logged in set done to True
#    ciao = 1

cli.close()