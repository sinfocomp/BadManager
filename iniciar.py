#!/usr/bin/python3
menu="\033[41;1;37m"
corPadrao="\033[0m"
preto="\033[0;30m"
vermelho="\033[0;31m"
verde="\033[0;32m"
marrom="\033[0;33m"
azul="\033[0;34m"
purple="\033[0;35m"
cyan="\033[0;36m"
cinzaClaro="\033[0;37m"
pretoCinza="\033[1;30m"
vermelhoClaro="\033[1;31m"
verdeClaro="\033[1;32m"
amarelo="\033[1;33m"
azulClaro="\033[1;34m"
purpleClaro="\033[1;35m"
cyanClaro="\033[1;36m"
branco="\033[1;37m"
fim="\033[0m"
versao=menu + "1.1.6" + fim
try:
	import os
	import platform
	import sys
	import subprocess
	sys.path.insert(0, "/etc/BadManager/")
	from criarusuario import criarusuario
	from deletarusuario import deletarusuario
	from limite import limite
	from backupusuario import backupusuario
	from debbackup import deb
	from servidor import configurar
	from criarusuariokey import criarusuariokey
except Exception as e:
	print(vermelho + "Error al importar modulos!" + fim)
	print(str(e))
	exit()

if platform.system() != "Linux":
	print(vermelho + "Esta utileria solo funciona en linux!" + fim)
	sys.exit(2)
else:
	subprocess.call("clear", shell=True)
	print(menu + "		 BADMANAGER {} 		 ".format(versao) + fim)

def menuscript():
	print(amarelo + "[1] Crear Usuario (ROOT)" + fim)
	print(amarelo + "[2] Borrar Usuario (ROOT)" + fim)
	print(amarelo + "[3] Poner limite de login a usuario (ROOT)" + fim)
	print(amarelo + "[4] Quitar limites de login a usuario (ROOT)" + fim)
	print(amarelo + "[5] Iniciar limites de login (ROOT)" + fim)
	print(amarelo + "[6] Respaldar todos los usuarios del sistema (ROOT)" + fim)
	print(amarelo + "[7] Restaurar todos los usuarios del sistema dede un respaldo (ROOT)" + fim)
	print(amarelo + "[8] Configurar SQUID3 (ROOT)" + fim)
	print(amarelo + "[9] Configurar SQUID (ROOT)" + fim)
	print(amarelo + "[10] Verificar informacion del sistema (ROOT)" + fim)
	print(amarelo + "[11] Hacer respaldo de todos los paquetes del sistema (ROOT)" + fim)
	print(amarelo + "[12] Restaurar respaldo de los paquetes del sistema (ROOT)" + fim)
	print(amarelo + "[13] configurar esta maquina para ser usada como servidor remoto" + fim)
	print(amarelo + "[14] conectar a un servidor remoto" + fim)
	print(amarelo + "[15] Modificar limite de login de usuario (ROOT)" + fim)
	print(amarelo + "[16] Monitor de usuarios (ROOT)" + fim)
	print(amarelo + "[17] Crear usuario con clave Publica (ROOT)" + fim)
	print(amarelo + "[18] Agregar Banner SSH (ROOT)" + fim)
	print(amarelo + "[19] Firewall con iptables customisado (TORRENT OFF)" + fim)
	print(amarelo + "[20] Compilar y configurar badvpn-udpgw" + fim)
	print(azul + "[000] Atualizar BadManager (ROOT)" + fim)
	print(vermelho + "[Ctrl+C] Sair" + fim)
	try:
		opcao = input(azul + "dijite su opcion: " + fim)
		if opcao == '':
			print(vermelho + "dijite una opcion!" + fim)
			menuscript()
		else:
			opcao = int(opcao)

	except KeyboardInterrupt:
		print(cyanClaro + "\nBye :P" + fim)
		exit(1)
	
	if opcao == 1:
		criarok = criarusuario.criarusuario()
		menuscript()
	elif opcao == 2:
		deletarok = deletarusuario.deletarusuario()
		menuscript()
	elif opcao == 3:
		addok = limite.deflimite()
		menuscript()
	elif opcao == 4:
		delok = limite.remlimite()
		menuscript()
	elif opcao == 5:
		gerok = limite.gerlimite()
		menuscript()
	elif opcao == 6:
		backupok = backupusuario.backupusuarios()
		menuscript()
	elif opcao == 7:
		restaurarok = backupusuario.restaurarusuarios()
		menuscript()
	elif opcao == 8:
		subprocess.call("sudo wget -q https://github.com/sinfocomp/scripts/raw/master/squid3-install && sudo bash squid3-install && rm -f squid3-install", shell=True)
		menuscript()
	elif opcao == 9:
		subprocess.call("sudo bash /etc/sinfocomp/squid/squid.sh", shell=True)
	elif opcao == 10:
		subprocess.call("sudo bash /etc/sinfocomp/system/system.sh", shell=True)
		menuscript()
	elif opcao == 11:
		deb.backup()
		menuscript()
	elif opcao == 12:
		deb.restaurar()
		menuscript()
	elif opcao == 13:
		configurar.configurar()
		menuscript()
	elif opcao == 14:
		configurar.conectar()
		menuscript()
	elif opcao == 15:
		subprocess.call("sudo bash /etc/BadManager/limite/mudlimite.sh", shell=True)
		menuscript()
	elif opcao == 16:
		subprocess.call("sudo bash /etc/BadManager/limite/monitor.sh", shell=True)
		menuscript()
	elif opcao == 17:
		criarusuariokey.criarusuariokey()
		menuscript()
	elif opcao == 18:
		subprocess.call("sudo bash /etc/BadManager/bannerssh/bannerssh.sh", shell=True)
		menuscript()
	elif opcao == 19:
		subprocess.call("sudo bash /etc/BadManager/firewall/firewall.sh", shell=True)
		menuscript()
	elif opcao == 20:
		subprocess.call("sudo bash /etc/BadManager/badvpn/badvpn-configurar.sh", shell=True)
		menuscript()
	elif opcao == 000:
		subprocess.call("sudo bash /etc/BadManager/atualizar/atualizar.sh", shell=True)
	else:
		print(vermelho + "Digiteuna opcion valida!" + fim)
		menuscript()

menuscript()

