from io import BytesIO
from gtts import gTTS
import pygame
import time
import streamlit as st
import cv2
import av
import requests
from ultralytics import YOLO
from streamlit_webrtc import webrtc_streamer



def main():
     car_detection_page = "Eagle eye"
     map_search_page = "information"
     app_mode = st.sidebar.selectbox(
          "Choose the app mode",
          [
               car_detection_page,
               map_search_page,
          ],
     )
     st.subheader(app_mode)
     if app_mode == car_detection_page:
          car_detection()
     elif app_mode == map_search_page:
          map_search()


def car_detection():
     model = YOLO("yolov8n.pt")

     def callback(frame):
          img = frame.to_ndarray(format = 'bgr24')
          

          results = model(
               img,
               classes=2,
               conf = 0.5
          )
          alerts = results[0]
          for alert in alerts:
               cls = int(alert.boxes.cls)
               if cls == 2:
                    f = BytesIO()
                    gTTS(text = "車体を検知しました", lang = "ja").write_to_fp(f)
                    f.seek(0)
                    pygame.mixer.init()
                    pygame.mixer.music.load(f)
                    pygame.mixer.music.play(1)
                    time.sleep(5)
                    continue
          time.sleep(2)
     webrtc_streamer(
     key="example",
     async_transform=True,
     media_stream_constraints={"video": True, "audio": False},
     video_frame_callback=callback
     )
def map_search():
     st.write("hello")
     st.map()
main()
