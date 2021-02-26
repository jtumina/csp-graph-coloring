#!/bin/bash
shopt -s nullglob
for f in graph-files/*; do
    echo "$f"
    python3 src/main.py "$f"
done
