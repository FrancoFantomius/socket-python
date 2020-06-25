import socket

max_h=10

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))#utlizzare la vera porta nella versione finale
s.listen(15)

while True:
    clientsocket, address=s.accept()
    print(f"{address}")
    msg="Connesso al Server"+str(address)
    msg=f"{len(msg):<{max_h}}"+msg
    clientsocket.send(bytes(msg, "utf-8"))
