import usb.core
import usb.util as util
import usb.backend.libusb1

backend = usb.backend.libusb1.get_backend(find_library=lambda x: "/usr/lib/libusb-1.0.so")

class ComUsb ():
    pass

# Comunicação USB

#dev = core.find(idVendor=0x1004) # Busca direto o dispostivo o dispositivo   # Comando no Linux - Lsusb       # Comando no Windows  - devmgmt.msc

dev =usb.core.find(find_all=True, backend=True) # Comando no Linux - Lsusb       # Comando no Windows  - devmgmt.msc
print(dev)

# Verifica se tem algum dispositivo
if dev is None:
    print('Dispositivo não encontrado')
    raise ValueError('Dispositivo não encontrado')

### até aqui funciona hahah

# Envia os dados para primeira usb que encontrar
dev.set_configuration()

# EndPoint
cfg = dev.get_active_configuration()
interface_number = cfg[(0,0)].bInterface_number
alternate_setting = usb.control.get_interface(interface_number)
intf = usb.util.find_descriptor(
    cfg, bTnerfaceNumber = interface_number,
    bAlternateSettings = alternate_setting
)

ep = usb.util.find_descriptor(
    intf,
    # match the first OUT endpoint
    custom_match = \
    lambda e:
        usb.util.endpoint_direction(e.bEndpointAddress) == \
        usb.util.ENDPOINT_OUT
)

assert ep is not None

# write the data
ep.write('test')