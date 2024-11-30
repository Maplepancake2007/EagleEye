FROM python:3.12.0

WORKDIR /app

COPY requiments.txt .
RUN apt-get -y update && apt-get -y upgrade && \
    apt-get update && apt-get install libgl1\
    apt install -y python3 python3-pip\
    pip3 install opencv-python


RUN pip install -r requirements.txt

EXPOSE 8501

COPY . /app

ENTRYPOINT ["streamlit","run"]
CMD ["EagleEye.py"]
