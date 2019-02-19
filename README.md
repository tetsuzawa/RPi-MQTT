# LINE or WEBサイトからRaspbeery PiのGPIOを操作

## プログラム構成
line_app.pyがメインのFlaskアプリ
line_app.pyが各モジュールを利用

## 必要知識
### pythonのモジュール  
- flask
- RPi.GPIO
- re (正規表現)
### その他
- git
- heroku
    - cloud mqtt
    - dyno
    - heroku config (環境変数（セキュリティ用）)
- line messaging API
    - line-bot-sdk-python
- mqtt
    - publisher (heroku上のflaskアプリに実装)
    - subscriber (ラズパイでpythonプログラムを常時実行j)
    - broker (herokuのcloud mqttがこれにあたる)


