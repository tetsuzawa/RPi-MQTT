from flask import Flask, render_template, request
import numpy as np
import os
from modules import pub04
#from modules import led_flash

app = Flask(__name__)

# メッセージをランダムに表示するメソッド
def picked_up():
    messages = [
        "こんにちは、あなたの名前を入力してください",
        "やあ！お名前は何ですか？",
        "あなたの名前を教えてね"
    ]
    # NumPy の random.choice で配列からランダムに取り出し
    return np.random.choice(messages)


@app.route('/', methods=['GET'])
def index():
    pub04.pub_main()
    return render_template('index.html')


@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'GET':
        res = request.args.get('get_value')
    elif request.method == 'POST':
        res = request.form['post_value']

    return res

@app.route('/switch', methods=['POST'])
def switch():
    res = request.form['post_value']
    message = picked_up()
    #led_flash.flash()
    return render_template('index.html') + res + message

if __name__ == '__main__':
    app.debug = True
    #app.run(host='192.168.0.81', port=8080)
    #app.run(host="localhost", port=8080)
    #app.run(host=process.env.PORT)
    port = int(os.environ.get('PORT', 500))
    app.run(host='0.0.0.0', port=port)
