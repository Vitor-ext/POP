from Conexao import serialApp

# Objeto para SerialApp
app = serialApp()

# Atualiza as portas do dispositivo
app.updatePort()

# Conexão
app.connectSerial()

# Recebe Buffer do Serial
contador = 0
while(1):
    app.readSerial()
    if(contador>=10): break
    contador +=1

# Fechando a Conexão
app.closeSerial()


     #ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=0)
     #while True:
     #    if state == "0":
     #     print "OK - Sem Alertas"
     #     sys.exit(0)
     #   elif (str(ser.read()) == '2'):
     #     print "WARNING "
     #    sys.exit(1)
     #   elif (str(ser.read()) == '1'):
     #     print "CRITICAL - Intrusos Detectados"
     #     sys.exit(2)
     #   else:
     #     print "UKNOWN - Parametro Desconhecido"
     #     sys.exit(3)