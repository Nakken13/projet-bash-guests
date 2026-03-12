#!/usr/bin/env python3

import json
import os
import time
import psutil
import subprocess

cpu = psutil.cpu_percent(interval=1)
disk = psutil.disk_usage('/').percent 
script_dir = os.path.dirname(os.path.abspath(__file__))
ram_process = subprocess.run(["bash", os.path.join(script_dir, "sonde-ram.sh")], capture_output=True, text=True)
ram = int(ram_process.stdout.strip())
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
