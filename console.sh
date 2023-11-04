#!/bin/bash

python3 /remote_console.py \
    --host 127.0.0.1 \
    --port ${RCON_PORT} \
    --password ${RCON_PASSWORD}
