from Conexao import serialApp
from flask import Flask
import json
import socket
import time


host = "127.0.0.1"  #Server address IPV4 da maquina na rede
port = 1235 #Port of Server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port)) #bind server
s.listen(100)
print('Webserver Ativo')

# Objeto para SerialApp
ser = serialApp()

# Atualiza as portas do dispositivo
ser.updatePort()
print('Atualizando Portas')

#Definindo Portas COM
ser.serialPort.port = 'COM3'
ser.serialPort.baudrate = 9600

# Conexão
ser.connectSerial()

#Recebe Buffer do Serial

while True:
    with open("status.json", encoding='utf-8') as status:     # Teste com Json
        dados = json.load(status)
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
        time.sleep(0.5)




### Aplicação Ficara no NUC, Atentar a questão de server client / levantar um servidor com host e porta ###


# Fechando a Conexão
#app.closeSerial()
#print('Conexão Fechada')

