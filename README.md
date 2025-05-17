# 🤖 Telegram Auto Post Bot — Mobile Dev News Daily 📱🚀

📌 Bot Telegram yang secara otomatis memposting berita terbaru tentang **Android**, **iOS**, dan **Flutter** ke grup Telegram developer setiap hari.  
Bot ini berjalan 100% gratis di **GitHub Actions**, tanpa perlu server, dan bisa kamu kustomisasi sesuka hati!

---

## ✨ Fitur Utama

✅ Ambil berita dari **banyak sumber terpercaya**  
✅ Otomatis jalan tiap hari (jam 9 pagi WIB)  
✅ Bisa kirim manual lewat tombol `Run workflow`  
✅ Tanpa biaya, tanpa hosting, tanpa ribet  
✅ Mudah diubah untuk topik atau komunitas lain

---

## 📰 Sumber Berita yang Digunakan

| Sumber                                                        | Topik                 | Format     | Status   |
| ------------------------------------------------------------- | --------------------- | ---------- | -------- |
| 🟢 [Dev.to](https://dev.to)                                   | Android, iOS, Flutter | JSON API   | ✅ aktif |
| 🟠 [Hacker News](https://hn.algolia.com/api)                  | Umum, Mobile, Tools   | JSON API   | ✅ aktif |
| 🔵 [Medium - Flutter](https://medium.com/feed/flutter)        | Flutter               | RSS → JSON | ✅ aktif |
| 🔴 [Reddit r/androiddev](https://www.reddit.com/r/androiddev) | Android               | RSS → JSON | ✅ aktif |

---

## ⚙️ Arsitektur Singkat

```
GitHub Actions (schedule/workflow_dispatch)
     |
     V
auto_post.py
     |
     +--> Ambil berita dari Dev.to
     +--> Kalau gagal, fallback ke HN → Medium → Reddit
     |
     V
Kirim ke Grup Telegram via Bot API
```

---

## 📂 Struktur Project

```
.
├── auto_post.py                # Script utama pengambil & pengirim berita
└── .github/
    └── workflows/
        └── daily.yml          # Konfigurasi GitHub Actions
```

---

## 🪜 Step-by-Step Setup Guide

### 1. 🧠 Buat Bot Telegram

- Buka [@BotFather](https://t.me/BotFather)
- Kirim: `/newbot` → beri nama & username
- Dapatkan `BOT TOKEN`

### 2. ➕ Tambahkan Bot ke Grup Telegram

- Tambahkan ke grup
- Jadikan **admin**
- Nonaktifkan privacy mode:  
  `/mybots → pilih bot → Bot Settings → Group Privacy → Turn Off`

### 3. 🆔 Dapatkan Chat ID Grup

- Kirim pesan di grup
- Buka:  
  `https://api.telegram.org/bot<BOT_TOKEN>/getUpdates`
- Ambil `"chat": { "id": -100xxxxxxxxxx }` → itu `TELEGRAM_CHAT_ID`

### 4. 🛠️ Fork & Clone Repo

```bash
git clone https://github.com/elnasio/telegram-auto-post.git
cd telegram-auto-post
```

### 5. 🔐 Tambahkan Secrets ke GitHub

| Name                 | Value                             |
| -------------------- | --------------------------------- |
| `TELEGRAM_BOT_TOKEN` | dari @BotFather                   |
| `TELEGRAM_CHAT_ID`   | ID grup, contoh: `-1001234567890` |

### 6. ✅ Pastikan Struktur File

```
.
├── auto_post.py
└── .github/
    └── workflows/
        └── daily.yml
```

### 7. 🚀 Jalankan Workflow Manual

- Buka tab **Actions** di GitHub
- Pilih: **"Kirim Berita Tiap Hari"**
- Klik tombol **Run workflow**

### 8. 🔄 Otomatis Setiap Hari

- GitHub akan menjalankan bot tiap jam **09:00 WIB**
- Tidak perlu VPS, PC nyala, atau cron job manual

---

## 💬 Contoh Output Telegram

```
📰 Understanding Navigation in Jetpack Compose
https://dev.to/username/article-url

🔥 Flutter Performance Tips from Hacker News
https://hn.link/article
```

---

## 📈 Rencana Fitur Selanjutnya

- [ ] Deteksi duplikat konten sebelum kirim
- [ ] Kirim multi-artikel sekaligus
- [ ] Simpan histori ke database (Supabase)
- [ ] Kirim ringkasan mingguan ke grup
- [ ] Ekspor konten ke WhatsApp (eksperimental)

---

## 📣 Credits

Made with ❤️ by [@elnasio](https://github.com/elnasio)  
Powered by **Python**, **GitHub Actions**, and the **Telegram Bot API**

---

## 🙋‍♂️ Author

Created and maintained by [@elnasio](https://www.linkedin.com/in/moriesdeohutapea)  
Feel free to connect or give credit when you use or fork this project 🙌
