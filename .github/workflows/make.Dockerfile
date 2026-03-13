FROM python:3.14-slim

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get upgrade -y && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN python -m pip install --root-user-action ignore --upgrade pip
RUN python -m pip install --root-user-action ignore --upgrade uv

COPY . /app

WORKDIR /app

ENTRYPOINT ["make"]
