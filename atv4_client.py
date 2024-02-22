import xmlrpc.client
import socket

s = xmlrpc.client.ServerProxy('http://10.0.84.187:21212')

s.armazenar(socket.gethostname())
s.armazenar("teste")
s.armazenar("teste 2")
s.armazenar("teste 3")

print(s.getMensagens())
print(s.getServerIp())
print(s.getDataTime())
print(s.quantidadeReq())
