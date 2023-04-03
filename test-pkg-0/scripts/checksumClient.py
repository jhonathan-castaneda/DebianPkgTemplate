#!/usr/bin/env python3

from pydbus import SystemBus   
from gi.repository import GLib
import os
#----------------------INSTANTIATE SYSTEM BUS
bus  = SystemBus()
BUS  = "com.monitoreointeligente.retotecnico"# << BUS_NAME
loop = GLib.MainLoop()

def callback(*args):
    #CALLBACK TO HANDLE SIGNAL "terminado"
    data=args[4]
    print("RECEIVED:{}".format(data))
    loop.quit()


if __name__=="__main__":

    print("CHECKSUM CLIENT HAS STARTED")
    filter = "/" + "/".join(BUS.split("."))
    print(filter)
    print("                           ")
    bus.subscribe(object = filter, signal_fired = callback)

    flag = 1

    while(flag==1):

        path = input("RUTA ABSOLUTA DEL ARCHIVO:")
        if (path == 'salir'):
            flag=0
            break

        method = input("MÉTODO DE COMPROBACIÓN A USAR:")
        if (method == 'salir'):
            flag=0
            break
        
        if (flag ==1):
            os.system('gdbus call --system --dest com.monitoreointeligente.retotecnico --object-path '+
            '/com/monitoreointeligente/retotecnico --method com.monitoreointeligente.retotecnico.calcular '+
            path +' '+ method )
            loop.run() 
