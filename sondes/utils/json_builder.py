#!/usr/bin/env python3

import json
import os
import time
import subprocess

DIR  = os.path.dirname(os.path.abspath(__file__))


nbr_process = subprocess.run("who | sort | cut -d' ' -f1 | uniq | wc -l", shell=True, capture_output=True, text=True)
nbr = int(nbr_process.stdout.strip())

cpu_process = subprocess.run([os.path.join(DIR, "sonde-cpu.py")], capture_output=True, text=True)
cpu = float(cpu_process.stdout.strip())

disk_process = subprocess.run([os.path.join(DIR, "sonde-disk.py")], capture_output=True, text=True)
disk = float(disk_process.stdout.strip())

ram_process = subprocess.run(["bash", os.path.join(DIR, "sonde-ram.sh")], capture_output=True, text=True)
ram = int(ram_process.stdout.strip())

final_json = {
    "user": os.environ.get("USER"),
    "server": os.uname()[1],
    "number_of_users": nbr,
    "data": [
        {
            "timestamp": int(time.time()),
            "sondes": {
                "cpu": cpu,
                "disk": disk,
                "ram": ram
            }
        }
    ]
}

print(json.dumps(final_json, indent=4))