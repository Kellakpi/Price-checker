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
    url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html" # Get the website url
    response = requests.get(url) #
    html = response.text
    soup = BeautifulSoup(html, "lxml")
    price_tag = soup.find ("p", class_="price_color") # Find the element
    price_text = price_tag.text.strip() # Strips and get the text in this case the number
    price = float(price_text[2:]) #Turn the number into a float. Could be "2:" or "1:" depending on characters before the currency sign

    #Shows the logic in your terminal, for visuals.
    if price < target_price:
        print(f"It went down! {price}!") 
    else:
        print(f"NO DEAL! HOOLD {price}!")
    
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN") #Loads telegram API Token
    chat_id = os.getenv("TELEGRAM_CHAT_ID") # Loads telegram Chat ID.
    message = f"Current price is £{price}. Still too high!"
    message2 = f"DEAL! Price dropped to £{price} — buy now!" #Custom messages on price status

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage" # Selects wich message to send based on status.
    if price > target_price:
        data = {"chat_id": chat_id, "text": message}
    else:
        data = {"chat_id": chat_id, "text": message2}

    response = requests.post(url, data=data) # Sends the message and prints it out for visibility
    print("Telegram message sent!")
    print("Status:", response.status_code)
    print("Response:", response.text)

#Main schedulers
schedule.every().day.at("16:00").do(send_telegram)

#Main looper
while True:
        schedule.run_pending()
        time.sleep(60)