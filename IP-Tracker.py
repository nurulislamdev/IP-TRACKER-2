#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import os
import sys
import requests
import json
import socket
from colorama import Fore, Style

GREEN = '\033[1;32m'
WHITE = '\033[1;37m'
RED = '\033[1;31m'
END = '\033[0m'

os.system("clear")

def banner():

	print(GREEN + Style.NORMAL +'''        
                          ██╗██████╗                       
                          ██║██╔══██╗                      
                          ██║██████╔╝                      
                          ██║██╔═══╝                       
                          ██║██║                           
                          ╚═╝╚═╝                           
                                                         
  ████████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ 
  ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
     ██║   ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝
     ██║   ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
     ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
     ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
             \033[0;32m====================================\033[0m
              \033[1;37mCREADOR:\033[0m R3LI4NT
              \033[1;37mGITHUB:\033[0m https://github.com/R3LI4NT
             \033[0;32m====================================\033[0m
'''+ END)

banner()

target = input(GREEN +"Ingresa la IP / URL: "+ END)
os.system("clear")
banner()


ip = socket.gethostbyname(target)
print("\033[0;32mLa dirección ip de [\033[0m\033[1;37m" +target+ "\033[0m\033[0;32m] es: [\033[0m\033[1;37m" +ip+ "\033[0m\033[0;32m]\033[0m\n")


respuesta = requests.get("http://ip-api.com/json/" +ip)
datos = respuesta.text
valores = json.loads(datos)

print("\033[0;32mIP:\033[0m", valores.get('query','No disponible'))
print("\033[0;32mESTADO / STATUS:\033[0m",  valores.get('status','No disponible'))
print("\033[0;32mPAÍS / COUNTRY:\033[0m", valores.get('country','No disponible'))
print("\033[0;32mCÓDIGO DE PAÍS / COUNTRY CODE:\033[0m", valores.get('countryCode','No disponible'))
print("\033[0;32mREGION:\033[0m", valores.get('region','No disponible'))
print("\033[0;32mCIUDAD / CITY:\033[0m", valores.get('city','No disponible'))
print("\033[0;32mCÓDIGO POSTAL / ZIP:\033[0m", valores.get('zip','No disponible'))
print("\033[0;32mZONA HORARIA / TIMEZONE :\033[0m", valores.get('timezone','No disponible'))
print("\033[0;32mPROVEDOR DE SERVICIOS / ISP NAME:\033[0m", valores.get('isp','No disponible'))
print("\033[0;32mLATITUD:\033[0m", str(valores.get('lat','No disponible')))
print("\033[0;32mLONGITUD:\033[0m", str(valores.get('lon','No disponible')))
print(" ")
