from flask import Flask, request, jsonify
import hmac
import hashlib
import base64
import logging
import os
from dotenv import load_dotenv

app = Flask(__name__)

# 用你的 Channel Secret 替换
load_dotenv()
CHANNEL_SECRET = os.getenv("Line_Channel_secret")

logging.basicConfig(level=logging.DEBUG)

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        # 验证签名
        signature = request.headers['X-Line-Signature']
        body = request.get_data(as_text=True)
        logging.info(f"Request body: {body}")
        
        hash = hmac.new(CHANNEL_SECRET.encode('utf-8'), body.encode('utf-8'), hashlib.sha256).digest()
        valid_signature = base64.b64encode(hash).decode('utf-8')

        if signature != valid_signature:
            return 'Invalid signature', 403

        # 处理 LINE Bot 传来的消息
        events = request.json['events']
        for event in events:
            if event['type'] == 'message':
                reply_token = event['replyToken']
                message = event['message']['text']
                logging.info(f"Received message: {message}")
                # 发送回覆逻辑

        return jsonify({'status': 'success'}), 200
    except Exception as e:
        logging.error(f"Error: {str(e)}")
        return 'Internal Server Error', 500

if __name__ == '__main__':
    app.run(port=5000)
