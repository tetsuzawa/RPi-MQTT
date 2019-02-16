from flask import Flask, request, abort
import numpy as np
import os
from modules import pub_line


from linebot import (
    LineBotApi, WebhookHandler, exceptions
)
from linebot.exceptions import (
    InvalidSignatureError, LineBotApiError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, QuickReplyButton, QuickReply, MessageAction 
)

app = Flask(__name__)

#環境変数取得
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    return "hello world!"


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: \n" + body)
    """
    try:
        print(type(body))
        print(str(body))
        print(body)

    except Exception as e:
        print(e)
        pass
    """

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    """
    try:
        print(event)
        print(type(event))
        print("\n\nevent.message" + str(event.message))
    except Exception as e:
        print(e)
    try:
        print(str(event))
    except Exception as e:
        print(e)
    """
    try:
        if event.message.text == 'gpio':
            text_message = TextSendMessage(text = "what colors would you like?",
                                            quick_reply = QuickReply(items = [
                                                QuickReplyButton(action=MessageAction(label="blue", text="text"))
                                            ]))
            line_bot_api.reply_message(
                event.reply_token,
                text_message
            )
        else:
            text_message = event.message.text
            pub_line.pub_test02(text_message)

            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=text_message)
            )

    except exceptions.LineBotApiError as e:
        print("start error handling")
        print(e.status_code)
        print(e.error.message)
        print(e.error.details)
        print("end")
 
    #pub_line.pub_main()
    """
    try:
        pub_line.pub_test02(event.message.text)
            
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=text_message)
        )
    except Exception as e:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=e)
        )
    """
        


if __name__ == "__main__":
#    app.run()
    app.debug = True
    #app.run(host='192.168.0.81', port=8080)

    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)