import os
import requests


TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


r = requests.post(f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage', json={
    'chat_id': TELEGRAM_CHAT_ID,
    'text': f'Starting <a href="https://github.com/GMDProjectL/iso-builder/actions">building</a> the ISO... ',
    'parse_mode': 'HTML'
})