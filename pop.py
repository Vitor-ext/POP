from Conexao import serialApp
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

# Conexão
ser.connectSerial()

#Recebe Buffer do Serial

while True:
    with open("status.json", encoding='utf-8') as status:     # Teste com Json
        dados = json.load(status)
    for i in dados:
        valor = (i['I0'])
        print(valor)
        print('Webserver Ativo')
        time.sleep(10)




### Aplicação Ficara no NUC, Atentar a questão de server client / levantar um servidor com host e porta ###


# Fechando a Conexão
#app.closeSerial()
#print('Conexão Fechada')

