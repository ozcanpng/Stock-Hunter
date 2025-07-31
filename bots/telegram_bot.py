import requests
from config import BOT_TOKEN, CHAT_ID

def send_telegram_message(message: str):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    try:
        r = requests.post(url, data={"chat_id": CHAT_ID, "text": message}, timeout=10)
        if r.status_code == 200:
            print("[📬] Telegram bildirimi gönderildi ✅")
        else:
            print(f"[❌] Telegram hata: {r.status_code} – {r.text}")
    except Exception as e:
        print(f"[💥] Telegram bağlantı hatası: {e}")
