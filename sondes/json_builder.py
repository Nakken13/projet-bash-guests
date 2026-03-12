#!/usr/bin/env python3

import json
import os
import time
import psutil
import subprocess

cpu = psutil.cpu_percent(interval=1)
disk = psutil.disk_usage('/').percent 
ram_process = subprocess.run(["bash", "./sonde-ram.sh"], capture_output=True, text=True)
ram = int(ram_process.stdout.strip()) 

final_json = {
    "user": os.environ.get("USER"),
    "server": os.uname()[1],
    "data": [
        {
            "timestamp": int(time.time()),
            "sondes":{
                "cpu": str(cpu) + "%",
                "disk": str(disk) + "%",
                "ram": str(ram) + "%"
            }
        }
    ]
}
print(json.dumps(final_json, indent=4))