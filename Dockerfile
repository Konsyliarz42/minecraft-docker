FROM eclipse-temurin:17
WORKDIR /server

RUN apt update \
    && apt install -y python3.11 pip \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir \
    pydantic-settings==2.0.3 \
    rcon==2.4.4

COPY ./set_properties.py /
COPY ./remote_console.py /

COPY ./console.sh /
RUN ["chmod", "+x", "/console.sh"]

COPY ./entrypoint.sh /
RUN ["chmod", "+x", "/entrypoint.sh"]

ENTRYPOINT ["/entrypoint.sh"]
