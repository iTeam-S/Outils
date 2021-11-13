#!/bin/bash

# recuperation valeur
username=$1
password=$2

# Creation de compte avec mot de passe
useradd -m $username
echo "$username:password" | chpasswd

# Creation compte mysql avec ermission DB ITEAMS
mysql -u iteams -p$ITEAMS_PASS -e "GRANT ALL PRIVILEGES ON ITEAMS.* TO $username@'%' identified by \"$password\";"
