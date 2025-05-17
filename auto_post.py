import os
import requests
import random

# Ambil dari environment GitHub Secrets
TOKEN = os.environ['TELEGRAM_BOT_TOKEN']
CHAT_ID = os.environ['TELEGRAM_CHAT_ID']
TAGS = ['android', 'ios', 'flutter']

def ambil_berita():
    tag = random.choice(TAGS)
    url = f"https://dev.to/api/articles?tag={tag}&per_page=5"
    try:
        res = requests.get(url)
        res.raise_for_status()
        data = res.json()
        if not data:
            return f"Tidak ada artikel ditemukan untuk tag: {tag}"
        artikel = random.choice(data)
        return f"📰 {artikel['title']}\n{artikel['url']}"
    except Exception as e:
        return f"Gagal mengambil berita: {e}"


def kirim_pesan(teks):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    response = requests.post(url, data={
        'chat_id': CHAT_ID,
        'text': teks
    })
    if response.status_code != 200:
        print("❌ Gagal kirim ke Telegram:", response.text)
    else:
        print("✅ Pesan berhasil dikirim.")

if __name__ == "__main__":
    pesan = ambil_berita()
    kirim_pesan(pesan)
