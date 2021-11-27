#/bin/bash

# recuperation de l'emplacement du script en cours
SCRIPT_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# lancement du script via ssh
ssh root@iteam-s.mg 'bash -s' < $SCRIPT_DIR/script.sh $@