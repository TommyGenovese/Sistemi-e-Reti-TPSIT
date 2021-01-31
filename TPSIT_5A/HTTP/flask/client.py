import requests, sys, socket
IpAddress = '127.0.0.1'
port = 5000
url ="http://"
#STREAM dato che è tcp e conncetion per connettersi al server con porta e IP prec. specificati
cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cli.connect((IpAddress, port))
done = False
while not done:
    password="lupus"
    body = "InputUsername=Tommy&InputPassword="+password
    bodylen= str(len(body))
    richiesta = """POST http://127.0.0.1:5000/login HTTP/1.1\r
    content_type: application/x-www-form-urlencoded\r
    Host: http://127.0.0.1:5000\r
    Content_lenght: """+bodylen+"""\r
    \n
    """+body
    r = requests.post(url, password)
    print(richiesta)
    cli.sendall(richiesta.encode())

    if done: #if i'm logged in set done to True
        ciao = 1

cli.close()