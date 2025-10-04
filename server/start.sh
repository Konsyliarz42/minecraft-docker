#!/bin/sh
set -e

# Overwrite eula file
echo "eula = ${EULA}" > /server/eula.txt

# Set require properties
if [ -e /server/server.properties ]; then
cat >> /server/server.properties<< EOF
enable-rcon=true
rcon.password=${RCON_PASSWORD}
rcon.port=${RCON_PORT}
server-port=${SERVER_PORT}
EOF
fi

# Start server
java -Xmx${SERVER_MEMORY} -jar /server/${SERVER_JAR} nogui
