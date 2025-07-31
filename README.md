# 🕵️‍♂️ Stock Hunter

**Telegram-powered multi-product tracking system**

Track Zara, Pull&Bear, and Bershka products in any size — get notified instantly when stock arrives!

---
## 🚀 Features

- 🔎 **Multi-Product Support**: Track multiple products and sizes simultaneously.

- 🤖 **Telegram Notifications**: Receive notifications via Telegram when stock is available.

- 🧠 **Automatic Brand Recognition**: Automatically distinguishes Zara / Pull&Bear / Bershka from the URL.

- 🛠️ **Selenium-Powered Automation**: Shadow DOM and dynamic content are successfully analyzed.

- ⚙️ **Works on All Platforms**: Compatible with Windows, Mac, and Linux.

- 📦 **Compilable as EXE**: Thanks to `builder.py`, you can create an .exe file with a single click.

---

## 🖥️ Installation

### 1. Install Required Packages

```bash

pip install -r requirements.txt

```

### 2. Enter Telegram Information (`config.py`)

```python

BOT_TOKEN = "{{BOT_TOKEN}}"

CHAT_ID = "{{CHAT_ID}}"

```

Or if you want to do it automatically:

```bash

python builder.py

```

---

## ✅ Usage

```bash

python main.py

```

- You can enter multiple product sizes, such as `https://www.zara.com/...` and `L`.

- Clicking on the blank line will start tracking.

- When the product is back in stock, you will receive a message from Telegram and the product will be removed from the list.

---

## 🛠️ Compilation (To Create an EXE)

```bash

python builder.py

```

This command:

- Embeds the TOKEN and CHAT ID in `config.py`

- Creates the `main.exe` file with `pyinstaller`

> Created file: `dist/main.exe`

---

## 📂 Project Structure

```

stockHunter/

├── builder.py

├── config.py

├── main.py

├── utils/

├── bots/

├── trackers/

└── requirements.txt

```

---

## 📸 Screenshot

```

🔍 🔴 ZARA - Checking size L...

[🧪] S — AVAILABLE

[❌] L — UNAVAILABLE

[🧪] XL — AVAILABLE

🎉 IN STOCK! 🎉

✅ Size: XL

🔗 URL: https://www.zara.com/...

📬 Telegram notification sent!

```

---

## 👨‍💻 Developer

**ozcanpng**

📫 [ozcanpng](https://github.com/ozcanpng)

---

## 📜 License

This project is for educational and personal use. Unauthorized commercial use is prohibited.
