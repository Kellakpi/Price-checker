import os
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import schedule
import time
import requests


load_dotenv()

target_price = 40.00


def send_telegram():
    url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"

    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, "lxml")

    price_tag = soup.find ("p", class_="price_color")

    price_text = price_tag.text.strip()
    price = float(price_text[2:])

    if price < target_price:
        print(f"It went down! {price}!")
    else:
        print(f"NO DEAL! HOOLD {price}!")
    
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    message = f"Current price is £{price}. Still too high!"
    message2 = f"DEAL! Price dropped to £{price} — buy now!"

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

    if price > target_price:
        data = {"chat_id": chat_id, "text": message}
    else:
        data = {"chat_id": chat_id, "text": message2}

    response = requests.post(url, data=data)
    print("Telegram message sent!")
    print("Status:", response.status_code)
    print("Response:", response.text)

#Main schedulers
schedule.every(1).seconds.do(send_telegram)

#Main looper
while True:
        schedule.run_pending()
        time.sleep(1)