#!/bin/python3
import json
import time
import psutil
import os
# possibilité d'envoyer les données récupées et les récupérer sur le moniteur et le moniteur peut intérroger

#cron : permet de lancer un programme tout les x temps

class SondeCpu:
    def __init__(self):
        self.cpu_percent = psutil.cpu_percent(interval=1) #récup infos du cpu
        self.time = int(time.time())#dater avec epoch
        self.name_server = os.uname()[1]#recup nom du server
        
    def collecter(self):
        return json.dump({
            "[INFO : CPU]": {
                "serveur": self.name_server,
                "temps": self.time,
                "cpu": self.cpu_percent
            }
        })

sonde = SondeCpu()
print(sonde.collecter())

