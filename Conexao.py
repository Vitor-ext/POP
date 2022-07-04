import serial
import serial.tools.list_ports

class serialApp ():
    def __init__(self):
        self.serialPort = serial.Serial()
        self.baudrate = [9600, 115200]
        self.portlist = []

    def updatePort(self):
        try:
            self.serialPort.open()
        except:
            print("Houve um erro ao abrir a porta serial")

    def sendSerial(self, data):
        if(self.serialPort.isOpen()):
            dadoSend = str(self.data)+ '\n'
            self.serialPort.write(dadoSend.enconde())
            self.seralPort.flushOutput()

    def readSerial(self):
        dataRead = self.serialPort.read().decode
        print(dataRead)

    def closeSerial(self):
        self.serialPort.close()

