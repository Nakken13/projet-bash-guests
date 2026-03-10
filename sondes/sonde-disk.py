#!/usr/bin/env python3

import psutil
import time
import os
import json
import os
import psutil
import time


class SondeDisque:
    def __init__(self):
        # récup % d'utilisation de la partition racine
        self.disk_percent = psutil.disk_usage('/').percent 
        self.time = int(time.time()) # dater avec epoch
        self.name_server = os.uname()[1] # recup nom du server

    def collecter(self):
        return json.dumps({
            "[INFO : DISQUE]": {
                "serveur": self.name_server,
                "temps": self.time,
                "disque": self.disk_percent
            }
        })

sonde = SondeDisque()
print(sonde.collecter())