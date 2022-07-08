import xml.etree.cElementTree as ET
import socket
from Conexao import serialApp

host = "127.0.0.1"  #Server address IPV4 da maquina na rede
port = 1235 #Port of Server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port)) #bind server
s.listen(100)
print('Webserver Ativo')

# Objeto para SerialApp
app = serialApp()

# Atualiza as portas do dispositivo
app.updatePort()

# Conexão
app.connectSerial()

# Recebe Buffer do Serial

while True:
    app.readSerial()

### Aplicação Ficara no NUC, Atentar a questão de server client / levantar um servidor com host e porta ###
  #  conn, addr = s.accept()
  #  dados = (str.encode('Enviando dados para o abastece'))
  #  conn.sendall(dados)
  #  valor = conn.recv(1)
  #  print(valor.decode())
  #  teste  = int (valor.decode())




# Fechando a Conexão
#app.closeSerial()

print('Parei Aqui')

#print('Conexão Fechada')

