#!/bin/sh
set -e

# Send to server to save and stop server
rcon -H localhost -p ${RCON_PORT} -P ${RCON_PASSWORD} stop
