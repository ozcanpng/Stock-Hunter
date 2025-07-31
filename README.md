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

---

![](https://github.com/ozcanpng/Stock-Hunter/blob/main/images/stockHunter.png)

## 🌟 Features

- 🔎 **Multi-Product Tracking**: Monitor multiple products and sizes simultaneously
- 🤖 **Smart Telegram Notifications**: Instant alerts when your desired size is back in stock
- 🧠 **Automatic Brand Detection**: Seamlessly supports Zara, Pull&Bear, and Bershka URLs
- 🛡️ **Advanced Web Scraping**: Handles dynamic content, shadow DOM, and anti-bot measures
- 💾 **Persistent Configuration**: Saves your Telegram credentials for future use
- 🎨 **Beautiful CLI Interface**: Colorful, user-friendly command-line experience
- ⚡ **Cross-Platform**: Works on Windows, macOS, and Linux
- 📦 **Ready-to-Use**: Windows users can download pre-compiled .exe file

---

## 🚀 Quick Start

### Option 1: Pre-compiled Windows Executable
1. Download `stockHunter.exe` from [Releases](https://github.com/ozcanpng/Stock-Hunter/releases)
2. Install [Chrome browser](https://www.google.com/chrome/) (required)
3. Download [ChromeDriver](https://chromedriver.chromium.org/) and place it in your PATH
4. Run `stockHunter.exe`

### Option 2: Python Source Code (All Platforms)

#### Prerequisites
- Python 3.8 or higher
- Google Chrome browser
- ChromeDriver (must be in PATH or same directory)

#### Installation
```bash
# Clone the repository
git clone https://github.com/ozcanpng/stockHunter.git
cd stockHunter

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

---

## 🛠️ Setup Guide

### 1. Telegram Bot Setup
1. Create a Telegram bot:
   - Message [@BotFather](https://t.me/BotFather) on Telegram
   - Send `/newbot` and follow instructions
   - Save your **Bot Token**

2. Get your Chat ID:
   - Message [@userinfobot](https://t.me/userinfobot) on Telegram
   - Save your **Chat ID**

### 2. ChromeDriver Setup
- **Windows**: Download from [ChromeDriver](https://chromedriver.chromium.org/) and place in same folder as executable
- **macOS**: `brew install chromedriver`
- **Linux**: `sudo apt-get install chromium-chromedriver`

---

## 📖 Usage

1. **Launch the application**
   ```bash
   python main.py
   # or run stockHunter.exe on Windows
   ```

2. **Enter Telegram credentials** (first time only)
   - Bot Token: `1234567890:AAA...`
   - Chat ID: `123456789`

3. **Add products to track**
   ```python
   Format: URL, SIZE
   Example: https://www.zara.com/tr/product-name, L
   
   [1] ➤ https://www.zara.com/tr/jacket, XL
   [2] ➤ https://www.pullandbear.com/tr/shirt, M
   [3] ➤ (leave empty to start tracking)
   ```

4. **Monitor the tracking**
   - The app will check stock every 5 seconds
   - When stock is found, you'll get a Telegram notification
   - Successfully tracked items are automatically removed

---

## 🎯 Supported Brands

| Brand | Website | Status |
|-------|---------|--------|
| **Zara** | zara.com | ✅ Full Support |
| **Pull&Bear** | pullandbear.com | ✅ Full Support |
| **Bershka** | bershka.com | ✅ Full Support |

---

## 📱 Example Output

```
🔄 Scanning Cycle #1
───────────────────────────────────────────────────────────────────────────────
🔍 🔴 ZARA - Checking size L... (3 products remaining)
🧁 Cookie check in progress...
✅ Cookie accepted.
👕 Loading sizes...
[🧪] S (US S)        — AVAILABLE
[❌] L (US L)        — OUT OF STOCK
[🧪] XL (US XL)      — AVAILABLE
   ❌ Out of stock - retrying in 5s

🔍 🟢 PULL&BEAR - Checking size M... (2 products remaining)
[🧪] XS   — AVAILABLE
[🧪] S    — AVAILABLE
[🧪] M    — AVAILABLE

                            🎉 STOCK FOUND! 🎉
╔═══════════════════════════════════════════════════════════════════════════════╗
║ ✅ Size: M                     ║
║ 🔗 URL:   https://www.pullandbear.com/tr/shirt...                ║
╚═══════════════════════════════════════════════════════════════════════════════╝
✔️  M size tracking completed.
```

---

## 📁 Project Structure

```
stockHunter/
├── main.py                 # Main application entry point
├── requirements.txt        # Python dependencies
├── telegram_bot.txt       # Auto-generated credentials file
├── utils/
│   └── driver_setup.py    # Chrome WebDriver configuration
├── bots/
│   └── telegram_bot.py    # Telegram notification handler
├── trackers/
│   ├── zara.py           # Zara-specific tracking logic
│   ├── pullandbear.py    # Pull&Bear tracking logic
│   └── bershka.py        # Bershka tracking logic
└── dist/                  # Compiled executables (if built)
    └── stockHunter.exe
```

---

## 🔧 Advanced Configuration

### Custom Scan Interval
Edit `main.py` line 158:
```python
interval = 10  # Change from 5 to 10 seconds
```

### Silent Mode (No Colors)
Set environment variable:
```bash
export NO_COLOR=1
```

---

## ❓ Troubleshooting

### Common Issues

**❌ ChromeDriver not found**
```
Solution: Download ChromeDriver and add to PATH or place in same directory
```

**❌ Telegram notifications not working**
```
Solution: Verify Bot Token and Chat ID are correct
- Test your bot by messaging it directly
- Ensure chat ID includes negative sign if it's a group
```

**❌ "Element not found" errors**
```
Solution: Websites may have updated their structure
- Check for updates to Stock Hunter
- Report the issue with the specific URL
```

**❌ High CPU usage**
```
Solution: Increase scan interval in main.py (line 158)
```

---

## 🚧 Development

### Building from Source
```bash
# Install development dependencies
pip install pyinstaller

# Build executable
pyinstaller --onefile --name stockHunter main.py

# Executable will be in dist/stockHunter.exe
```

### Contributing
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📜 Legal Notice

This tool is for **educational and personal use only**. Please respect the terms of service of the websites you're tracking. The developer is not responsible for any misuse of this software.

---

## 👨‍💻 Developer

<div align="center">

**Made with ❤️ by [ozcanpng](https://github.com/ozcanpng)**

[![GitHub](https://img.shields.io/badge/GitHub-ozcanpng-black?style=for-the-badge&logo=github)](https://github.com/ozcanpng)

*If this project helped you, consider giving it a ⭐!*

</div>

---

<div align="center">

### 🎯 Happy Hunting! 

*Never miss your favorite items again*

</div>
