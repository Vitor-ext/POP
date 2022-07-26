from Conexao import Conexao
from Usb import Usb
from Log import Log
from flask import Flask
import json
import xml.etree.ElementTree as xml
from xmlrpc.server import SimpleXMLRPCServer
import time

class pop ():
##################  Construção do Servidor   ####################
#    host ="127.0.0.1"  #Server address IPV4 da maquina na rede
#    port = 1235 #Port of Server


##################  Caso Queira Utilizar a Porta Serial   ####################
# Objeto para SerialApp
    Con = Conexao()

##################  Instanciando USB   ####################
# Objeto para Usb
    Usb = Usb()

##################  Instanciando Log   ####################
# Objeto para Usb
    Log = Log()

##################  Registrando no Log Inicio    ####################
    Log.logger.info("Servço Iniciado")




# Seguir com o xml iniciar avanços
    while True:
        status = "status.xml"
    dados = xml.parse(status)
    root = dados.getroot()
    filtro = "*"
    #print(root.iter.child.text)
    for child in root.iter(filtro):
        print(child.tag, child.text)
        Log.logger.info(child.tag and child.text)
        #Log.logger.debug(child.text)
    time.sleep(1)


server = SimpleXMLRPCServer(("localhost", 1235))
server.register_function(pop, "pop")
server.serve_forever()

##################  Salvando Log para Consulta    ####################

   # Log.logger.info("Servço Iniciado")
   # Log.logger.error(child.text)




### Aplicação Ficara no NUC, Atentar a questão de server client / levantar um servidor com host e porta ###

