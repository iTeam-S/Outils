#!/bin/bash

# Script de deployement auto dans le serveur principal de iTeam-$

# enchainement des parametres 
source ./parametre.conf

# Recuperation du projet
git clone $REPOS "$DOSSIER_INSTALLATION/$NOM_PROJET"

# Installations des dependances
eval $INSTALL_DEPENDANCE

if [ -z $DEPLOYEMENT ]; then
    eval $DEPLOYEMENT_COMMANDE
else 
    cp $SERVICE_FILE /etc/systemd/system/
    systemctl enable $SERVICE_FILE
    systemctl start $SERVICE_FILE
fi
