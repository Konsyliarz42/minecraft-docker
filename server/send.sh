#!/bin/sh
set -e

rcon -H localhost -p ${RCON_PORT} -P ${RCON_PASSWORD} $@
