import os
import requests
import random

TOKEN = os.environ['TELEGRAM_BOT_TOKEN']
CHAT_ID = os.environ['TELEGRAM_CHAT_ID']
TAGS = ['android', 'ios', 'flutter']

def ambil_berita():
    tag = random.choice(TAGS)
    url = f"https://dev.to/api/articles?tag={tag}&top=1"
    res = requests.get(url)
    if res.status_code != 200:
        return f"Gagal mengambil berita dengan tag {tag}."
    data = res.json()
    if not data:
        return f"Tidak ada artikel ditemukan dengan tag {tag}."
    artikel = data[0]
    return f"📰 {artikel['title']}\n{artikel['url']}"

def kirim_pesan(teks):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={'chat_id': CHAT_ID, 'text': teks})

if __name__ == "__main__":
    kirim_pesan(ambil_berita())
