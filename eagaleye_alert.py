import js2py
import streamlit as st

# Define some JavaScript code
js_code = """
function locate {
    navigator.geolocation.getCurrentPosition(successCallback, errorCallback);
};
function successCallback(position){
    // 緯度を取得し画面に表示
    var latitude = position.coords.latitude;
    // 経度を取得し画面に表示
    var longitude = position.coords.longitude;
};

// 取得に失敗した場合の処理
function errorCallback(error){
    alert("位置情報が取得できませんでした");
};

var result = locate();
"""

context = js2py.EvalJs()
result = context.execute(js_code)

# Print the result
st.title(context.result)