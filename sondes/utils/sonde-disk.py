#!/usr/bin/env python3

import psutil

disk = psutil.disk_usage('/').percent
print(disk)