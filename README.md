# Price Drop Notifier

A Python script that checks the price of a product from a website and notifies you via **Telegram** when it drops below your target! I mixed what i learned on my other projects to make this one, im proud of it.

---

## Features

- Scrapes real-time price data using **BeautifulSoup**
- Sends Telegram alerts when the price drops
- Scheduled to run daily at a specific time
- Easy configuration using `.env` for API tokens and chat ID

---

## How It Works

1. Fetches a product page from a website (`books.toscrape.com`)
2. Parses the current price
3. Compares it to your desired price
4. Sends a Telegram message:
   - If price is **too high**: you get a reminder
   - If price **drops below** your threshold: you get an alert to buy 

---

## Requirements

>bash
pip install -r requirements.txt

---

# Tech used
- requests

- bs4 (BeautifulSoup)

- schedule

- dotenv

- Telegram Bot API

---

Built by @Kellakpi