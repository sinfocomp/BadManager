
#!/bin/bash

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

if [ ! -f /etc/limite/limite.txt ]
then
echo -e "$vermelho
Debe agregar un usuario antes de poder modificarlo!$fim"
exit 2
else
echo ""
fi
echo -e "$menu
Cambiar limite de usuario:$fim"

usuario=$(cat /etc/limite/limite.txt | awk '{print $1" Limite: "$2}')

echo "$usuario"
read -p "nombre de usuario para modificar limite: " usuariolimite
if [ ! "$(cat /etc/limite/limite.txt | grep -w $usuariolimite)" ]
then
echo -e "$vermelho
Por favor escriba un nombre de usuario valido!$fim"
exit
fi

read -p "Escriva nuevo limite $usuariolimite: " usuariolimite2



novolimite="$(echo $usuariolimite $usuariolimite2 && cat /etc/limite/limite.txt | grep -wv "$usuariolimite")"
echo "$novolimite" > /etc/limite/limite.txt
echo -e "$cyan
Limite cambiado!$fim"
exit 1
fi
