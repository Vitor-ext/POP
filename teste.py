import usb.core
import usb.util as util
import usb.backend
import pyusb_libusb1_backend
import array

backend = usb.backend.libusb1.get_backend(find_library=lambda x: "C:\Windows\System32\MS64\dll\libusb-1.0.dll")

VID = 0X000
PID = 0X000

dev =usb.core.find(idVendor=VID, idProduct=PID, backend=backend)    # Comando no Linux - Lsusb       # Comando no Windows  - devmgmt.msc

# Verifica se tem algum dispositivo
if dev is None:
    print('Dispositivo não encontrado')
else:
    print('Dispositivo encontrado')

#ep=dev[0].interfaces()[0].endpoints()[0]
#i=dev[0].interfaces()[0].bInterfaceNumber
#dev.reset()

#if dev.is_kernel_driver_active():
#    dev.detach_kernel_driver()

#dev.set_configuration()
#eaddr=ep.bEndpointAddress

#r=dev.read(eaddr, 100)
#print(len(r))

