FROM python:3.9

RUN apt-get update && apt-get install -y \
    ffmpeg \
    libgl1 \
 && rm -rf /var/lib/apt/lists/*

ENV POETRY_VIRTUALENVS_IN_PROJECT=false

RUN pip install -r requirements.txt

WORKDIR /srv

RUN poetry install
