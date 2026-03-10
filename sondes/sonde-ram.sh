#!/bin/bash

serveur=$(hostname)
temps=$(date +%s)
# Calcul du pourcentage de RAM utilisée
ram=$(free | awk '/Mem:/ {printf("%.0f"), $3/$2 * 100}')

echo "{\"[INFO : RAM]\": {\"serveur\": \"$serveur\", \"temps\": $temps, \"ram\": $ram}}"