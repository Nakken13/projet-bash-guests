#!/bin/python3
import time
import psutil
import os
# possibilité d'envoyer les données récupées et les récupérer sur le moniteur et le moniteur peut intérroger

#cron : permet de lancer un programme tout les x temps

class SondeCpu:
    def __init__(self):
        self.cpu_percent = psutil.cpu_percent(interval=1) #récup infos du cpu

    def collecter(self):
        return self.cpu_percent

sonde = SondeCpu()
print(sonde.collecter())

