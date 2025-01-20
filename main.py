import subprocess
import time
import os

# 启动 Discord 机器人
def run_discord_bot():
    return subprocess.Popen(['python', 'discord_bot.py'])

# 启动 LINE Webhook 处理程序
def run_webhook():
    return subprocess.Popen(['python', 'webhook.py'])

# 启动 ngrok
def run_ngrok():
    # 确保 ngrok 在 PATH 中
    return subprocess.Popen(['ngrok', 'http', '5000'])

if __name__ == "__main__":
    # 启动 Discord 机器人
    discord_bot_process = run_discord_bot()
    time.sleep(8)  # 等待 Discord 机器人启动

    # 启动 Webhook
    webhook_process = run_webhook()
    time.sleep(8)  # 等待 Webhook 启动

    # 启动 ngrok
    ngrok_process = run_ngrok()

    # 等待进程完成
    discord_bot_process.wait()
    webhook_process.wait()
    ngrok_process.wait()
