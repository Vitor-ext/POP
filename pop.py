from Conexao import Conexao
from Usb import Usb
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
    with open("status.xml", encoding='utf-8') as status:     # Teste com Xml
        dados = xml.parse(status)
    for i in dados:
        I0 = (i['I0'])
        I1 = (i['I1'])
        O0 = (i['O0'])
        O1 = (i['O1'])
        print(" Valor da Variavel IO", I0, "\n",
              "Valor da Variavel I1", I1, "\n",
              "Valor da Variavel O0", O0,"\n",
              "Valor da Variavel O1", O1)
        print('Webserver Ativo em 127.0.0.1:1235')
        time.sleep(60)




### Aplicação Ficara no NUC, Atentar a questão de server client / levantar um servidor com host e porta ###

