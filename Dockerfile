FROM nvcr.io/nvidia/l4t-base:r32.7.1

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    python3-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN python3 -m pip install --no-cache-dir --upgrade pip setuptools wheel
RUN python3 -m pip install --no-cache-dir \
    pymodbus==2.1.0 \
    mysql-connector-python==8.0.28 \
    fastapi \
    uvicorn

WORKDIR /app
