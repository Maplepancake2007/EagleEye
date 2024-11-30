FROM python:3.12.0

WORKDIR /app

COPY requiments.txt .
RUN apt update\
    apt install -y libopencv-dev

RUN pip install --upgrade pip\
    pip install -r requirements.txt\
    pip install opencv-python


EXPOSE 8501

COPY . /app

ENTRYPOINT ["streamlit","run"]
CMD ["EagleEye.py"]
