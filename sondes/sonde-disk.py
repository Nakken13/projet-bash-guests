#!/usr/bin/env python3

import psutil
import time
import os
import time


class SondeDisque:
    def __init__(self):
        # récup % d'utilisation de la partition racine
        self.disk_percent = psutil.disk_usage('/').percent 

    def collecter(self):
        return self.disk_percent

sonde = SondeDisque()
print(sonde.collecter())