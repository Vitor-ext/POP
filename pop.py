from Conexao import Conexao
from Usb import Usb
from Log import Log
from flask import Flask
import json
import xml.etree.ElementTree as xml
import time


##################  Construção do Servidor   ####################
host = "127.0.0.1"  #Server address IPV4 da maquina na rede
port = 1235 #Port of Server


##################  Caso Queira Utilizar a Porta Serial   ####################
# Objeto para SerialApp
Con = Conexao()

##################  Instanciando USB   ####################
# Objeto para Usb
Usb = Usb()

##################  Instanciando Log   ####################
# Objeto para Usb
Log = Log()

# Atualiza as portas do dispositivo
##ser.updatePort()
##print('Atualizando Portas Seriais')

#Definindo Portas COM
##ser.serialPort.port = 'COM3'
##ser.serialPort.baudrate = 9600

# Conexão
##ser.connectSerial()

# Seguir com o xml iniciar avanços
while True:
    status = "status.xml"
    dados = xml.parse(status)
    root = dados.getroot()
    filtro = "*"
    #print(root.iter.child.text)
    for child in root.iter(filtro):
        print(child.tag, child.text)
    #    time.sleep(0.5)

##################  Salvando Log para Consulta    ####################

    Log.logger.error("Servço Iniciado")
    Log.logger.error("status.xml")




### Aplicação Ficara no NUC, Atentar a questão de server client / levantar um servidor com host e porta ###

