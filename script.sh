#!/bin/bash

read -p "Entrez le premier nom : " nom1
read -p "Entrez le deuxième nom : " nom2
read -p "Entrez le troisième nom : " nom3

if [ "$nom1" = "ahmed" ] && [ "$nom2" = "atigh" ] && [ "$nom3" = "medmoctar" ]; then
    echo "ce projet est réaliser par $nom1, $nom2 et $nom3"
else
    echo "les noms ne sont pas corrects"
fi
