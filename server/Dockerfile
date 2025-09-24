FROM alpine:3.22.1
WORKDIR /server

# Install packages
RUN apk add --update --no-cache openjdk21-jre rcon nano

# Copy server scripts and create symbolic links
COPY server/start.sh server/stop.sh /
RUN ln -s /start.sh /usr/bin/start \
    && ln -s /stop.sh /usr/bin/stop

# Start server as default behaviour
CMD [ "start" ]
