from flask import Flask, request, abort
import numpy as np
import os
import re
#パブリッシャーのインポート
from modules import pub_line
from modules.re_compiler import ReMatch
#LINEBotのSDKのインポート
from linebot import (
    LineBotApi, WebhookHandler, exceptions
)
from linebot.exceptions import (
    InvalidSignatureError, LineBotApiError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, QuickReplyButton, QuickReply, MessageAction 
)

#Flaskのインスタンスの作成
app = Flask(__name__)

#環境変数取得
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

#動作確認用ウェブサイトのルーティング
#アクセスすると hello world! を表示
@app.route("/", methods=['GET', 'POST'])
def hello_world():
    return "hello world!"


#LINEからのWebhookを処理
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: \n" + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


#送られてきたものがテキストメッセージのときの処理
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    
    #送られてきたメッセージの中身の取り出し
    text_message = event.message.text

    #gpio を含んだメッセージが送られてきた場合, クイックリプライメニューを送信
    #その他はオウム返し
    gpio = ReMatch(text_message, 'gpio')

    try:
        if gpio.match:
            sending_object = send_quick_reply_button()

        else:
            pub_line.pub_line_message(text_message)
            sending_object = TextSendMessage(text=text_message)

        line_bot_api.reply_message(
            event.reply_token,
            sending_object
        )

    except exceptions.LineBotApiError as e:
        print("start error handling")
        print(e.status_code)
        print(e.error.message)
        print(e.error.details)
        print("end")
 

#クイックリプライメニューを送信する関数
def send_quick_reply_button():

    quick_reply_content = TextSendMessage(text = "what colors would you like?",
                                        quick_reply = QuickReply(items = [
                                            QuickReplyButton(action=MessageAction(label="blue", text="Flash blue")),
                                            QuickReplyButton(action=MessageAction(label="yellow", text="Flash yellow")),
                                            QuickReplyButton(action=MessageAction(label="alternately", text="Flash alternately"))
                                        ]))

    return quick_reply_content
        


#起動
if __name__ == "__main__":
    app.debug = True

    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)