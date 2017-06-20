import subprocess
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
def deflimite():
	usuario=input(verde + "Ingresa nombre de usuario para limitar: " + fim)
	limite=str(input(verde + "Limite para usuario logins: " + usuario + ": " + fim))
	subprocess.call("sudo bash /etc/BadManager/limite/deflimite.sh " + usuario + " " + limite, shell=True)

def remlimite():
	subprocess.call("sudo bash /etc/BadManager/limite/remlimite.sh", shell=True)

def gerlimite():
	resposta = input(cyan + "Desea iniciar el limitador en pantalla (y/n): " + fim)
	if resposta == "y" or resposta == "Y":
		try:
			iniciar = input(cyan + "Desea que el limitador al iniciar sistema? (y/n): " + fim)
			if iniciar == "y" or iniciar == "Y":
				subprocess.call("sudo echo '#!/bin/bash' > /etc/init.d/limite", shell=True)
				subprocess.call("sudo echo 'bash /etc/BadManager/limite/limite.sh &' >> /etc/init.d/limite", shell=True)
				subprocess.call("sudo chmod a+x /etc/init.d/limite", shell=True)
				subprocess.call("sudo chmod a+x /etc/BadManager/limite/limite.sh", shell=True)
				subprocess.call("sudo update-rc.d limite defaults", shell=True)
			subprocess.call("sudo screen bash /etc/BadManager/limite/limite.sh", shell=True)
		except KeyboardInterrupt:
			print(azul + "Bye :P" + fim)
			exit()
	elif resposta == "n" or resposta == "N":
		try:
			subprocess.call("sudo bash /etc/BadManager/limite/limite.sh", shell=True)
		except KeyboardInterrupt:
			print(azul + "Bye :P" + fim)
			exit()
	else:
		print(vermelho + "Por favor ingese opcion valida!" + fim)
		exit()
