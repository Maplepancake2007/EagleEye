// ボタンを押した時の処理
    // 位置情報を取得する
function locate(){
    navigator.geolocation.getCurrentPosition(successCallback, errorCallback);
};
// 取得に成功した場合の処理
function successCallback(position){
    // 緯度を取得し画面に表示
    var latitude = position.coords.latitude;
    printf(lantitude);
    // 経度を取得し画面に表示
    var longitude = position.coords.longitude;
    printf(longitude);
};

// 取得に失敗した場合の処理
function errorCallback(error){
    alert("位置情報が取得できませんでした");
};
locate()
