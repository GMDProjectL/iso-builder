import os
import subprocess
import requests


TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


for filename in os.listdir('out/'):
    print(f'Uploading {filename} to temp.sh ...')

    files = {
        'file': open(filename, 'rb'),
    }

    response = requests.post('https://temp.sh/upload', files=files)
    final_url = response.text

    print(f'\n\nUploaded: {filename} to {final_url}')

    r = requests.post(f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage', json={
        'chat_id': TELEGRAM_CHAT_ID,
        'text': f'Uploaded {filename} to {final_url}, it\'s temporary'
    })
