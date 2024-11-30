FROM python:3.12.0

WORKDIR /app

COPY requiments.txt .

RUN pip install -r requirements.txt

EXPOSE 8501

COPY . /app

ENTRYPOINT ["streamlit","run"]
CMD ["EagleEye.py"]
