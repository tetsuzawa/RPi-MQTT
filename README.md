# LINE or WEBサイトからRaspbeery PiのGPIOを操作

## プログラム構成
- line_app.py : メインのFlaskアプリ. herokuにデプロイ.
- sub.py : パブリッシュされたメッセージを受け取る. ラズパイ上で実行.
- modules/re_compiler.py LINEのメッセージを加工. herokuで実行
- modules/pub_line.py : LINEのメッセージをパブリッシュ. herokuで実行.  
- modules/led_flash.py : GPIOを操作.
- template/index.html : herokuのルートページ(/)にアクセスした際にレンダリングされるファイル.
- template/flash_button.html : herokuのGPIO操作ページ(/flash)にアクセスした際にレンダリングされるファイル.

## 理解に必要な知識
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


