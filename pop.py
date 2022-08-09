#from serial import *
#from server import webserver
from Usb.Usb import Usb
from Log.Log import Log
import xml.etree.ElementTree as xml
import time

class pop ():
    pass

##################  Caso Queira Utilizar a Porta Serial   ####################
# Objeto para SerialApp
    #Con = Cone

##################  Instanciando USB   ####################
# Objeto para Usb
    Usb = Usb()

##################  Instanciando Log  ' ####################
# Objeto para Usb
    Log = Log()

##################  Registrando no Log Inicio    ####################
    Log.logger.info("Serviço Iniciado")



# Seguir com o xml iniciar avanços
while True:
    # print (Usb.con())
    status = "templates/status.xml"
    dados = xml.parse(status)
    root = dados.getroot()
    filtro = "*"
    #print(root.iter.child.text)
    for child in root.iter(filtro):
        print(child.tag, child.text)
        Log.logger.info(child.tag)
        #Log.logger.debug(child.text)
    time.sleep(1)

##################  Salvando Log para Consulta    ####################

   # Log.logger.info("Serviço Iniciado")
   # Log.logger.error(child.text)
