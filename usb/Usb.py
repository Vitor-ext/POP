# coding=utf-8
import usb.core
import usb.util as util
import usb.backend.libusb1

backend = usb.backend.libusb1.get_backend(find_library=lambda x: "C:\Windows\System32\MS64\dll\libusb-1.0.dll")

class Usb ():
    pass

VID = 0x275d                # Codigo do fornecedor, tentar fazer a comunicação somente com ele.
#PID = 0x0Ba6


#Comunicação USB
#dev = list(usb.core.find(find_all=True, backend=backend))    # Comando no Linux - Lsusb       # Comando no Windows  - devmgmt.msc
dev = usb.core.find(IdVendor=VID, backend=backend)
#dev = usb.core.find(find_all=True, backend=backend)  # Encontra todos os dispositivos
print(dev)

# Verifica se tem algum dispositivo
if dev is None:
    print('Dispositivo não encontrado')
else:
    print('Dispositivo encontrado')

    dev.set_configuration()

    # EndPoint
    cfg = dev.get_active_configuration()
    intf = cfg[(0,0)]

    ep = usb.util.find_descriptor(
        intf,
        # match the first OUT endpoint
        custom_match = \
        lambda e: \
            usb.util.endpoint_direction(e.bEndpointAddress) == \
            usb.util.ENDPOINT_OUT)

    assert ep is not None


    ### Escrita na ESP32 - Modo Teste ###

#Postar o xml

    ep.write('test')


    ### Leitura da ESP32 - Modo Teste ###

    con = dev.read(1, 1024, 100) # Valor Lido da Placa    # (Endereço Final / Tamanho do dado esperado  / Timeout)