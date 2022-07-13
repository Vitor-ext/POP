import usb.core as core

# Comunicação USB

dev=core.find(IdVendo=0, IdProduct=0)  # Verificar Valores no LSCPU
ep=dev[0].interfaces()[0].endpoints()[0]
i=dev[0].interfaces()[0].bInterfaceNumber

dev.reset() # Reseta a condição atual do dispositivo

if dev.is_Kernel_driver_active(i):    # Verifica se o Dispositivo está ativo
    dev.detach_kernel_driver(i)

dev.set_configuration()
eaddr=ep.bEndpointAddress

r=dev.read(eaddr, 1024)
print(len(r))