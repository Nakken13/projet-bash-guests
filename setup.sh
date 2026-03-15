#!/usr/bin/bash
chmod +x ./sondes/sonde.sh
for f in ./sondes/utils/*.py; do
    chmod +x "$f"
done
