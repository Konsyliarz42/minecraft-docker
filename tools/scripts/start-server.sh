#!/bin/sh

PYTHONPATH=/ python -m server_tools --server && java -Xmx${MAX_MEMORY} -jar /server/${SERVER_JAR} nogui
