import os

#ANALISIS DE CONEXION 
hostname="www.itmorelia.edu.mx"
respuesta = os.system("ping -c 1 "+hostname)
if respuesta == 0 :
    print(hostname+": esta en funcionamiento!")
else:
    print(hostname+": No funciona!")

#DETECTAR COMPUTADORAS ACTIVAS
red = "200.33.171.0/24"
os.system("nmap -sP "+red)

"""
Starting Nmap 7.80 ( https://nmap.org ) at 2020-02-27 11:43 CST
Nmap scan report for mail.itmorelia.edu.mx (200.33.171.3)
Host is up (0.029s latency).
Nmap scan report for 200.33.171.13
Host is up (0.0096s latency).
Nmap scan report for 200.33.171.85
Host is up (0.056s latency).
Nmap scan report for 200.33.171.115
Host is up (0.070s latency).
Nmap scan report for 200.33.171.120
Host is up (0.036s latency).
Nmap done: 256 IP addresses (5 hosts up) scanned in 26.37 seconds
"""
