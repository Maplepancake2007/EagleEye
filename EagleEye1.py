from io import BytesIO
from gtts import gTTS
from  streamlit_folium import st_folium
from folium.plugins import Draw
import folium
import geojson
from geojson import dump
import streamlit.components.v1 as stc
import pyttsx3
from concurrent.futures import ThreadPoolExecutor
import threading
from streamlit.runtime.scriptrunner import add_script_run_ctx
from streamlit.components.v1 import html
from streamlit_javascript import st_javascript
from streamlit_js_eval import streamlit_js_eval, copy_to_clipboard, create_share_link, get_geolocation
import pygame
import time
import streamlit as st
import cv2
import av
import requests
import threading
from ultralytics import YOLO
from streamlit_webrtc import webrtc_streamer



def main():
     car_detection_page = "Eagle eye"
     infomation_page = "information"
     app_mode = st.sidebar.selectbox(
          "Choose the app mode",
          [
               car_detection_page,
               infomation_page,
          ],
     )
     st.subheader(app_mode)
     if app_mode == car_detection_page:
          main2()
     elif app_mode == infomation_page:
          infomation()

def main2():
     with ThreadPoolExecutor()as executor:
          executor.submit(car_detection)
          executor.submit(map_search)
          for t in executor._threads:
                add_script_run_ctx(t)


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
    with open("gjson.geojson") as f:
        #gj=geojson.load(f)
        gjsons = [geojson.load(f)] # 辞書型で取得
        f.close()
        

    # 地図の表示箇所とズームレベルを指定してマップデータを作成
    # attr（アトリビュート）は地図右下に表示する文字列。
    # デフォルトマップの場合は省略可能
    # 単色地図を使用する場合の例
    # attr（アトリビュート）は自分で適当な物を決定する。
    # 指定したアトリビュートは右下に表示される。

    def kenti(a,b,i):
        keido=gjsons[0]["features"][i]["geometry"]["coordinates"][0]
        ido=gjsons[0]["features"][i]["geometry"]["coordinates"][1]
        num=gjsons[0]["features"][i]["properties"]["category"]
        if num==1 and abs(a- ido) <= 5*8.983148616*10**-6 and abs(b-keido) <= 5*1.10966382364*10**-5:
                out=0
            #time.sleep(1)
        elif num==2 and abs(a- ido) <= 10*8.983148616*10**-6 and abs(b-keido) <= 10*1.10966382364*10**-5:
                out=0
        elif num==3 and abs(a- ido) <= 15*8.983148616*10**-6 and abs(b-keido) <= 15*1.10966382364*10**-5:
                out=0
        elif num==4 and abs(a- ido) <= 20*8.983148616*10**-6 and abs(b-keido) <= 20*1.10966382364*10**-5:
                out=0
        elif num==5 and abs(a- ido) <= 30*8.983148616*10**-6 and abs(b-keido) <= 30*1.10966382364*10**-5:
                out=0
        else:
            out=1
            #time.sleep(1)
        return out


    def gps(n): 
        time.sleep(5)
        loc=get_geolocation(component_key=n)
        lat=loc["coords"]['latitude']
        lng=loc["coords"]['longitude']
        return lat,lng

        
    def read_text(text):
        # エンジンの初期化
        engine = pyttsx3.init()

        # テキストを読み上げる
        engine.say(gjsons[0]["features"][text]["properties"]["name"])

        # 読み上げを実行
        engine.runAndWait()
        


    st.title('Eagle Eye')

    #ユーザーピン入力欄
    number = st.number_input('Choose a risk level.　The higher the number, the more dangerous it is.', 1,5)
    inputText=st.text_input(label="What dangers are there?",value="Danger")
    buttonA = st.button('Save Pin')


    try:
        x,y=gps(0)
    except:
        x=35.0
        y=137.0

    m = folium.Map(
        
        attr='Eagle Eye',
        location=[x,y],
        zoom_start=16
    )

    # 描画プラグインを有効化
    Draw(
        export=True,
        position='topleft',
        draw_options={
            'polyline': False,
            'rectangle': False,
            'polygon': False,
            'circle': False,
            'marker': True,
            'circlemarker': False
        }
    ).add_to(m)


    #危険箇所のピン
    for gjson in gjsons:
        #iconcolor=style_function(n)
        folium.GeoJson(gjson
        ).add_to(m)

    s=1 #component_key

    while True:
        i=0
        try:
            x,y=gps(s)
        except:
            pass





        #自分の位置

        folium.Marker(
            [x,y],
            popup='ME',
            tooltip='ME',
            icon=folium.Icon(color='red', icon='info-sign')
        ).add_to(m)


        folium.CircleMarker(
            [x,y],
            radius=10, 
            popup = "ME",
            color="red",
            fill=True,
            fill_color="red",
        ).add_to(m)


        #音が鳴る
        for i in range(len(gjsons[0]["features"])):
            out=kenti(x,y,i)
            if out==0:
                thread = threading.Thread(target=read_text, args=(i,))
                thread.start()
            # 音声合成が終わるまで待機
                thread.join()
                
            elif out==1:
                pass
            

        s=s+1

        # 地図データの描画
        st_data = st_folium(m, width=700, height=500)
        
        
        if buttonA:    
            j=[st_data]
            
            k=j[0]["last_active_drawing"]["geometry"]["coordinates"][0]
            l=j[0]["last_active_drawing"]["geometry"]["coordinates"][1]
            kikendo="abunai"
            
            with open("gjson.geojson") as f:
                gjsons = f.read() # 辞書型で取得
                f.close()
            gjpin=gjsons.removesuffix("]}")
            gjson=str(gjpin)
            #{"type": "Feature", "properties": {"name":"  ", "category":  }, "geometry": {"type": "Point", "coordinates": [  ,  ]}}
            g='{"type": "Feature", "properties": {"name":"'
            g1='","category":'
            g2='}, "geometry": {"type": "Point", "coordinates": ['
            a=','
            b=']}}'
            with open("gjson.geojson", mode='w') as f:
                f.write(gjpin)
                f.write(",")
                f.write(g)
                f.write(str(inputText))
                f.write(g1)
                f.write(str(number))
                f.write(g2)
                f.write(str(k))
                f.write(a)
                f.write(str(l))
                f.write(b)
                f.write("]}")
                f.close()


def infomation():
     st.write("hello")
if __name__=='__main__':
    main()
