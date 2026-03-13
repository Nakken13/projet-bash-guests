#!/usr/bin/env python3

import json
import os
import time
import subprocess

script_dir = os.path.dirname(os.path.abspath(__file__))

nbr_process = subprocess.run("who | sort | cut -d' ' -f1 | uniq | wc -l", shell=True, capture_output=True, text=True)
nbr = int(nbr_process.stdout.strip())

cpu_process = subprocess.run(["./sonde-cpu.py"], capture_output=True, text=True)
cpu = cpu_process.stdout.strip()

disk_process = subprocess.run(["./sonde-disk.py"], capture_output=True, text=True)
disk = disk_process.stdout.strip()

ram_process = subprocess.run(["bash", os.path.join(script_dir, "sonde-ram.sh")], capture_output=True, text=True)
ram = int(ram_process.stdout.strip())

final_json = {
    "user": os.environ.get("USER"),
    "server": os.uname()[1],
    "number of users": nbr,
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