# 🕵️‍♂️ Stock Hunter v2.0

<div align="center">

![Stock Hunter](https://img.shields.io/badge/Stock-Hunter-brightgreen?style=for-the-badge&logo=target)
![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-orange?style=for-the-badge&logo=selenium)
![Telegram](https://img.shields.io/badge/Telegram-Bot-blue?style=for-the-badge&logo=telegram)

**🎯 Multi-brand stock tracking system with instant Telegram notifications**

*Track Zara, Pull&Bear, and Bershka products in any size — get notified instantly when stock arrives!*

[📦 Download Latest Release](https://github.com/ozcanpng/Stock-Hunter/releases) • [🐛 Report Bug](https://github.com/ozcanpng/Stock-Hunter/issues) • [✨ Request Feature](https://github.com/ozcanpng/Stock-Hunter/issues)

</div>

![](https://github.com/ozcanpng/Stock-Hunter/blob/main/images/stockHunter.png)

---

## 🌟 Features

- 🔎 **Multi-Product Tracking**: Monitor multiple products and sizes simultaneously
- 🤖 **Smart Telegram Notifications**: Instant alerts when your desired size is back in stock
- 🧠 **Automatic Brand Detection**: Seamlessly supports Zara, Pull&Bear, and Bershka URLs
- 💾 **Persistent Configuration**: Saves your Telegram credentials for future use
- ⚡ **Cross-Platform**: Works on Windows, macOS, and Linux
- 📦 **Ready-to-Use**: Pre-compiled executables for Windows and macOS

---

## 🚀 Quick Start

### Windows
1. Download `stockHunter.exe` from [Releases](https://github.com/ozcanpng/Stock-Hunter/releases)
2. Install [Chrome browser](https://www.google.com/chrome/)
3. Download [ChromeDriver](https://chromedriver.chromium.org/) and add to PATH
4. Run `stockHunter.exe`

### macOS
1. Download `stockHunter_MacOS` from [Releases](https://github.com/ozcanpng/Stock-Hunter/releases)
2. Install [Chrome browser](https://www.google.com/chrome/)
3. Install ChromeDriver: `brew install chromedriver`
4. Open Terminal and run: `chmod +x stockHunter_MacOS`
5. **Important**: Go to System Settings → Privacy & Security → scroll down and allow the application to run
6. Run `./stockHunter_MacOS`

### Python Source (All Platforms)
```bash
git clone https://github.com/ozcanpng/stockHunter.git
cd stockHunter
pip3 install -r requirements.txt
python3 main.py
```

---

## 🛠️ Setup Guide

### Telegram Bot Setup
1. Create a bot: Message [@BotFather](https://t.me/BotFather) → `/newbot` → Save your **Bot Token**
2. Get Chat ID: Message [@userinfobot](https://t.me/userinfobot) → Save your **Chat ID**

### ChromeDriver Setup
- **Windows**: Download and place in PATH or same folder as executable
- **macOS**: `brew install chromedriver`
- **Linux**: `sudo apt-get install chromium-chromedriver`

---

## 📖 Usage

1. **Launch the application**
2. **Enter Telegram credentials** (first time only)
3. **Add products to track**
   ```
   Format: URL, SIZE
   Example: https://www.zara.com/tr/product-name, L
   ```
4. **Monitor tracking** - Get notifications when stock is found!

---

## 🎯 Supported Brands

| Brand | Website | Status |
|-------|---------|--------|
| **Zara** | zara.com | ✅ Full Support |
| **Pull&Bear** | pullandbear.com | ✅ Full Support |
| **Bershka** | bershka.com | ✅ Full Support |

---

## ❓ Troubleshooting

**ChromeDriver not found**
- Download ChromeDriver and add to PATH or place in same directory

**Telegram notifications not working**
- Verify Bot Token and Chat ID are correct
- Test your bot by messaging it directly

**macOS Security Issues**
- Run `chmod +x stockHunter_MacOS` in Terminal
- Allow the app in System Settings → Privacy & Security

---

## 📜 Legal Notice

This tool is for **educational and personal use only**. Please respect the terms of service of the websites you're tracking.

---

<div align="center">

**Made with ❤️ by [ozcanpng](https://github.com/ozcanpng)**

[![GitHub](https://img.shields.io/badge/GitHub-ozcanpng-black?style=for-the-badge&logo=github)](https://github.com/ozcanpng)

### 🎯 Happy Hunting! 
*Never miss your favorite items again*

</div>
