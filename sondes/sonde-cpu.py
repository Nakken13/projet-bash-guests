#!/usr/bin/env python3

import psutil

class SondeCpu:
    def __init__(self):
        self.cpu_percent = psutil.cpu_percent(interval=1) #récup infos du cpu

    def collecter(self):
        return self.cpu_percent

sonde = SondeCpu()
print(sonde.collecter())

