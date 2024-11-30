FROM python:3.12.0

WORKDIR /app

COPY requiments.txt .
RUN apt update\
    apt install -y libopencv-dev

RUN apt install -y python3 python3-pip
    pip install --upgrade pip\

RUN pip install -r requirements.txt
RUN pip install opencv-python


EXPOSE 8501

COPY . /app

ENTRYPOINT ["streamlit","run"]
CMD ["EagleEye.py"]
