#!/usr/bin/env python3
#-------------------------------------------
import argparse
import configparser
import hashlib
import os
from pydbus import SystemBus   
from pydbus.generic import signal   
from gi.repository import GLib

#----------------------INSTANTIATE SYSTEM BUS
bus  = SystemBus()
BUS  = "com.monitoreointeligente.retotecnico"# << BUS_NAME
loop = GLib.MainLoop()
#---------------------PRESET RECOGNIZED CHECKSUM METHODS(DICTIONARY 1)
global available
available = ['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512'] 
#------------------------------------------------------------------------------------------------------CHECKSUM METHODS
#CHECKSUM METHOD 1 (MD5)
def md5Sum(path):     
    with open(path, 'rb') as opened_file:
        x1 = opened_file.read()
        md5  = hashlib.md5()
        md5.update(x1)

    return(md5.hexdigest())

#CHECKSUM METHOD 2 (SHA1)
def sha1Sum(path):
    with open(path, 'rb') as opened_file:
        x2 = opened_file.read()
        sha1  = hashlib.sha1()
        sha1.update(x2)

    return(sha1.hexdigest())
    
#CHECKSUM METHOD 3 (SHA224)
def sha224Sum(path):  
    with open(path, 'rb') as opened_file:
        x3 = opened_file.read()
        sha224  = hashlib.sha224()
        sha224.update(x3)

    return(sha224.hexdigest())
    
#CHECKSUM METHOD 4 (SHA256)
def sha256Sum(path):
    with open(path, 'rb') as opened_file:
        x4 = opened_file.read()
        sha256  = hashlib.sha256()
        sha256.update(x4)

    return(sha256.hexdigest())

#CHECKSUM METHOD 5 (SHA384)
def sha384Sum(path):  
    with open(path, 'rb') as opened_file:
        x5 = opened_file.read()
        sha384  = hashlib.sha384()
        sha384.update(x5)

    return(sha384.hexdigest())

#CHECKSUM METHOD 6 (SHA512)
def sha512Sum(path):
    with open(path, 'rb') as opened_file:
        x6 = opened_file.read()
        sha512  = hashlib.sha512()
        sha512.update(x6)

    return(sha512.hexdigest())
#-------------------------------------------------------------------------------------------------------- (DICTIONARY 2)
global methods
methods = {"md5":md5Sum ,"sha1":sha1Sum, "sha224":sha224Sum, "sha256":sha256Sum, "sha384":sha384Sum, "sha512":sha512Sum}

#--------------------------------------------------------------------------------------METHOD 1. EMIT SIGNAL "terminado"
def broadcast(token, resultado, codigoerror, mensajeerror):
    print("{},{},{},{}".format(token, resultado, codigoerror, mensajeerror))
    emit.terminado(token, resultado, codigoerror, mensajeerror)
    return True
#-----------------------------------------------------------------------------------------------------CLASS DBUS SERVICE
class DBusService_XML(): 

    #DBUS SERVICE XML DEFINITION:
    dbus="""
    <node>
        <interface name = "com.monitoreointeligente.retotecnico">
            <method name = 'calcular'>
                <arg type = "s" name="ruta" direction="in"/>
                <arg type = "s" name="tiposuma" direction="in"/>
                <arg type = "s" name="respuesta" direction="out"/>
            </method>
            <signal name="terminado">
                <arg name="token"        type="s"/>
                <arg name="resultado"    type="s"/>
                <arg name="codigoerror"  type="u"/>
                <arg name="mensajeerror" type="s"/>
            </signal>
            <property name="solicitudesactivas" type="q" access="read"/>
            <property name="maximoactivas"      type="q" access="readwrite"/>
            
        </interface>
    </node>
    """.format(BUS)

    terminado = signal() # << "terminado" SIGNAL INSTANCE

    def calcular(self, ruta, tiposuma):
        try:
            if(tiposuma in available):     #CHECK FOR VALID CHECKSUM METHOD
                if(os.path.exists(ruta)):  #CHECK FOR VALID PATH TO ANALIZE A FILE

                    resultado = methods[tiposuma](ruta)
                    broadcast(tiposuma, resultado, 0, " ")
                    return ("{token:"+tiposuma+"}")
                    
                else:
                    error1="archivo para comprobación no encontrado en la ruta "+ruta+" (no existe el archivo)"
                    broadcast(tiposuma, " ", 1, error1 )
                    return("{token:"+" "+"{codigoerror:1},"+"{mensajeerror:"+error1+"}"+"}")
            else:
                error2 = "el método especificado para la suma de comprobación no está disponible (intentar con los siguentes:'md5' 'sha1' 'sha224' 'sha256' 'sha384' 'sha512')"
                broadcast(tiposuma, "", 2, error2 )
                return ("{token:"+" "+"{codigoerror:2},"+"{mensajeerror:"+error2+"}"+"}")
        except:
            pass

if __name__=="__main__":

    #IMPORT CONFIG FILE--------------------------------------------------------------------------------------------
    parser = argparse.ArgumentParser()
    parser.add_argument('--config',  type=str, default="/etc/test-pkg/config.ini", help = "(initial settings path) default: /etc/test-pkg/config.ini")
    args, unknown = parser.parse_known_args()
    print(args)

    #READ INITIAL SETTINGS FROM CONFIG FILE
    cf = configparser.ConfigParser()
    cf.read(args.config)  

    #SPIN------------------------------
    
    emit = DBusService_XML()
    bus.publish(BUS, emit)
    loop.run()
    """
    try:
        emit = DBusService_XML()
        bus.publish(BUS, emit)
        loop.run()
    except:
        pass
    """
