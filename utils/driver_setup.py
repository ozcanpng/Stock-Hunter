import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import platform
import shutil

load_dotenv()  # .env dosyasını oku

def find_chrome_binary():
    # .env varsa onu kullan
    chrome_path = os.getenv("CHROME_BINARY")
    if chrome_path and os.path.exists(chrome_path):
        return chrome_path

    # Otomatik tahmin (Mac / Windows / Linux)
    if platform.system() == "Darwin":  # macOS
        default_mac = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        return default_mac if os.path.exists(default_mac) else None

    elif platform.system() == "Windows":
        possible_paths = [
            os.path.expandvars(r"%ProgramFiles%\Google\Chrome\Application\chrome.exe"),
            os.path.expandvars(r"%ProgramFiles(x86)%\Google\Chrome\Application\chrome.exe")
        ]
        for path in possible_paths:
            if os.path.exists(path):
                return path
        return None

    elif platform.system() == "Linux":
        chrome_in_path = shutil.which("google-chrome") or shutil.which("chromium-browser")
        return chrome_in_path

    return None


def find_chromedriver():
    chromedriver_path = os.getenv("CHROMEDRIVER_PATH")
    if chromedriver_path and os.path.exists(chromedriver_path):
        return chromedriver_path

    # sistem PATH içinde chromedriver varsa onu kullan
    chromedriver = shutil.which("chromedriver")
    if chromedriver:
        return chromedriver

    # fallback
    if platform.system() == "Darwin":
        return "/usr/local/bin/chromedriver"
    elif platform.system() == "Windows":
        return "chromedriver.exe"
    elif platform.system() == "Linux":
        return "/usr/bin/chromedriver"

    return None


def setup_driver() -> webdriver.Chrome:
    opts = Options()
    opts.add_argument("--disable-gpu")
    opts.add_argument("--no-sandbox")

    chrome_binary = find_chrome_binary()
    if chrome_binary:
        opts.binary_location = chrome_binary
    else:
        raise RuntimeError("Chrome binary bulunamadı! `.env` içinde CHROME_BINARY ayarlayabilirsin.")

    chromedriver_path = find_chromedriver()
    if not chromedriver_path:
        raise RuntimeError("Chromedriver bulunamadı! `.env` içinde CHROMEDRIVER_PATH ayarlayabilirsin.")

    service = Service(chromedriver_path)
    return webdriver.Chrome(service=service, options=opts)
