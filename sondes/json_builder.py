#!/usr/bin/env python3

import json
import os
import time
import psutil
import subprocess

cpu = psutil.cpu_percent(interval=1)
disk = psutil.disk_usage('/').percent 
ram = subprocess.run("./sonde-ram.sh")

os.system("clear")

final_json = {
    "user": os.environ.get("USER"),
    "server": os.uname()[1],
    "data": [
        {
            "timestamp": int(time.time()),
            "sondes":{
                "cpu": cpu,
                "disk": disk,
                "ram": ram
            }
        }
    ]
}
print(json.dumps(final_json, indent=4))