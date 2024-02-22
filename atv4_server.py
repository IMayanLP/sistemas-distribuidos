from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import socket
import datetime

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

with SimpleXMLRPCServer(('10.0.84.187', 21212),requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    
    mensagens = []
    quantidadeReq = 0
    
    def armazenar(mensagem):
        mensagens.append(mensagem)
        quantidadeReq += 1
        return (True)
    
    def getServerIp():
        quantidadeReq += 1
        return (socket.gethostbyname(socket.gethostname()))
    
    def getDataTime():
        quantidadeReq += 1
        date = datetime.datetime.now()
        date_string = date.strftime("%A %d %B %y %I:%M")
        return date_string

    def getMensagens():
        quantidadeReq += 1
        return(mensagens)

    def getQtdReq():
        return quantidadeReq
    
    server.register_function(armazenar, 'armazenar')
    server.register_function(getMensagens, 'getMensagens')
    server.register_function(getServerIp, 'getServerIp')
    server.register_function(getDataTime, 'getDataTime')
    server.register_function(quantidadeReq, 'quantidadeReq')

    server.serve_forever()
