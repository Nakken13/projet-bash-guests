#!/bin/bash

serveur=$(hostname)
temps=$(date +%s)
user=$(whoami)
ram=$(free | awk '/Mem:/ {printf("%.0f"), $3/$2 * 100}')

echo "{\"[INFO : RAM]\": {\"serveur\": \"$serveur\", \"user\": \"$user\", \"temps\": $temps, \"ram\": $ram}}"