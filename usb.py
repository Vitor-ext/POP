import usb.core as core
import usb.util as util
import usb.backend.libusb1

backend = usb.backend.libusb1.get_backend(find_library=lambda x: "/usr/lib/libusb-1.0.so")

#class ComUsb ():

# Comunicação USB
dev= list(core.find(find_all=True, backend=True))  # Verificar Valores no LSCPU
print(dev)

# Verifica se tem algum dispositivo
if dev is None:
    print('Dispositivo não encontrado')
    #raise ValueError('Dispositivo não encontrado')

# Envia os dados para primeira usb que encontrar
dev.set_configuration()

# EndPoint
cfg = dev.get_active_configuration()
intf = cfg[(0,0)]

ep = util.find_descriptor(
    intf,
    # Combina com o primeiro EndPoint
    custom_match = \
    lambda e: \
        util.endpoint_direction(e.bEndpointAddress) == \
        util.ENDPOINT_OUT)

assert ep is not None

# Envia dados
ep.write('test')

