FROM python:3.12-alpine AS builder
WORKDIR /

# Install and configure poetry
RUN pip install --no-cache-dir poetry==1.8.5
ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

# Install packages
COPY pyproject.toml poetry.lock ./
RUN --mount=type=cache,target=$POETRY_CACHE_DIR poetry install --without dev --no-root


FROM python:3.12-alpine AS runtime
WORKDIR /server_tools

# Add python environment
COPY --from=builder /.venv .venv
ENV PATH="/server_tools/.venv/bin:$PATH"

# Install OpenJDK and nano
RUN apk add --update --no-cache openjdk21-jre nano

# Copy server tools and create symbolic links for scripts
COPY tools .
RUN chmod +x /server_tools/scripts/console.sh \
    && ln -s /server_tools/scripts/console.sh /usr/bin/console \
    && chmod +x /server_tools/scripts/start-server.sh \
    && ln -s /server_tools/scripts/start-server.sh /usr/bin/start-server

# Copy additional server files
COPY data /server
WORKDIR /server

# Start server as default behaviour
CMD [ "start-server" ]
