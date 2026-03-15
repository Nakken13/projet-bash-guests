#!/usr/bin/bash

for f in ./sondes/*.py; do
    chmod +x "$f"
done

for f in ./sondes/*.sh; do
    chmod +x "$f"
done