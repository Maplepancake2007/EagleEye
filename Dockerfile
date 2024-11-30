FROM python:3.12.0

WORKDIR /app

COPY requiments.txt .
RUN apt-get -y update && apt-get -y upgrade && \
    apt-get -y install python3-pip vim libgl1-mesa-dev libgtk2.0-dev && \
    pip3 install opencv-python


RUN pip install -r requirements.txt

EXPOSE 8501

COPY . /app

ENTRYPOINT ["streamlit","run"]
CMD ["EagleEye.py"]
