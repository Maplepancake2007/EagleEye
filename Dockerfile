FROM python:3.9

RUN apt-get update && apt-get install -y \
    ffmpeg \
    libgl1 \
 && rm -rf /var/lib/apt/lists/*
RUN apt-get install -y libgl1-mesa-dev

ENV POETRY_VIRTUALENVS_IN_PROJECT=false

RUN pip install -r requirements.txt

WORKDIR /
