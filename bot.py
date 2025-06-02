import os
import time
import requests

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

def send_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {'chat_id': CHAT_ID, 'text': text}
    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print("Сообщение отправлено")
        else:
            print(f"Ошибка при отправке: {response.status_code}, {response.text}")
    except Exception as e:
        print(f"Ошибка сети: {e}")

def main():
    while True:
        send_message("Тестовое сообщение от Флоки — бот работает!")
        time.sleep(60 * 10)  # Отправлять раз в 10 минут

if __name__ == "__main__":
    main()
