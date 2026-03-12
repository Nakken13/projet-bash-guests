import json
import os
import time

final_json = {
    "user": os.environ.get("USER"),
    "server": os.uname()[1],
    "data": [
        {
            "timestamp": int(time.time()),
            "sondes":{
                "cpu": os.system("./sonde-cpu.py"),
                "disk": os.system("./sonde-disk.py"),
                "ram": os.system("./sonde-ram.sh")
            }
        }
    ]
}
print(json.dumps(final_json, indent=4))