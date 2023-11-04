#!/bin/bash

echo "Setting required properties"
python3 /set_properties.py

java -Xmx${SERVER_MAX_MEMORY} -jar /server/${SERVER_JAR} nogui
