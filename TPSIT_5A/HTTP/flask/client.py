import socket
IpAddress = '127.0.0.1'
port = 5000
#STREAM dato che è tcp e conncetion per connettersi al server con porta e IP prec. specificati
cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cli.connect((IpAddress, port))
body = "InputUsername=Tommy&InputPassword=ciaociao"
body= str(len(body))
richiesta = """POST http://127.0.0.1:5000/login HTTP/1.1\r
content_type: application/x-www-form-urlencoded\r
Host: http://127.0.0.1:5000\r
Content_lenght: """+body+"""\r
\n
InputUsername=Tommy&InputPassword=ciaociao
"""
print(richiesta)
cli.sendall(richiesta.encode())

cli.close()