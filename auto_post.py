import os
import requests
import random

# Ambil token dan chat ID dari GitHub Secrets
TOKEN = os.environ['TELEGRAM_BOT_TOKEN']
CHAT_ID = os.environ['TELEGRAM_CHAT_ID']
TAGS = ['android', 'ios', 'flutter']

def ambil_dari_devto():
    tag = random.choice(TAGS)
    url = f"https://dev.to/api/articles?tag={tag}&per_page=5"
    res = requests.get(url, timeout=10)
    res.raise_for_status()
    data = res.json()
    if not data:
        raise Exception("Dev.to kosong")
    artikel = random.choice(data)
    return f"📰 {artikel['title']}\n{artikel['url']}"

def ambil_dari_hackernews():
    url = "https://hn.algolia.com/api/v1/search?query=flutter"
    res = requests.get(url, timeout=10)
    res.raise_for_status()
    data = res.json()
    artikel = data['hits'][0]
    return f"🔥 {artikel['title']}\n{artikel['url']}"

def ambil_dari_medium():
    rss_url = "https://medium.com/feed/flutter"
    api_url = f"https://api.rss2json.com/v1/api.json?rss_url={rss_url}"
    res = requests.get(api_url, timeout=10)
    res.raise_for_status()
    data = res.json()
    artikel = data['items'][0]
    return f"📘 {artikel['title']}\n{artikel['link']}"

def ambil_dari_reddit():
    rss_url = "https://www.reddit.com/r/androiddev/.rss"
    api_url = f"https://api.rss2json.com/v1/api.json?rss_url={rss_url}"
    res = requests.get(api_url, timeout=10, headers={"User-Agent": "telegram-bot"})
    res.raise_for_status()
    data = res.json()
    artikel = data['items'][0]
    return f"👥 {artikel['title']}\n{artikel['link']}"

def kirim_pesan(teks):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    res = requests.post(url, data={
        'chat_id': CHAT_ID,
        'text': teks
    })
    if res.status_code != 200:
        print("❌ Gagal kirim ke Telegram:", res.text)
    else:
        print("✅ Pesan berhasil dikirim.")

if __name__ == "__main__":
    sumber = [
        ambil_dari_devto,
        ambil_dari_hackernews,
        ambil_dari_medium,
        ambil_dari_reddit,
    ]

    for ambil in sumber:
        try:
            pesan = ambil()
            kirim_pesan(pesan)
            break
        except Exception as e:
            print(f"❌ Gagal dari sumber: {ambil.__name__} — {e}")
