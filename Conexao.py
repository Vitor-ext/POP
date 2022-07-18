import serial
import serial.tools.list_ports

class Conexao ():
    def __init__(self):
        self.serialPort = serial.Serial()
        self.baudrate = [9600, 115200]
        self.portlist = []

    # Metodo Update das Portas Seriais
    def updatePort(self):
        self.portlist = [port.device for port in serial.tools.list_ports.comports()]
        print(self.portlist)

    # Conexão
    def connectSerial(self):
        try:
            self.serialPort.open()
        except:
            print("Houve um erro ao abrir a porta serial")

    #Envia Dados
    def sendSerial(self, data):
        if(self.serialPort.isOpen()):
            dadoSend = str(self.data)+ '\n'
            self.serialPort.write(dadoSend.enconde())
            self.seralPort.flushOutput()

    #Recebe Dados
    def readSerial(self):
        dataRead = self.serialPort.read().decode
        print(dataRead)

    def closeSerial(self):
        self.serialPort.close()
