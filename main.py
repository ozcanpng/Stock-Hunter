from utils.driver_setup import setup_driver
from bots.telegram_bot import send_telegram_message
from trackers.pullandbear import PullAndBearTracker
from trackers.zara import ZaraTracker
from trackers.bershka import BershkaTracker
import time
import os
from colorama import Fore, Back, Style, init

# Colorama'yı başlat
init(autoreset=True)


def print_ascii_banner():
    # Gökkuşağı renkli ASCII banner
    banner = f"""
{Fore.CYAN}╔═══════════════════════════════════════════════════════════════════════════════╗
{Fore.CYAN}║                                                                               ║
{Fore.RED} ███████╗████████╗ ██████╗  ██████╗██╗  ██╗    
{Fore.YELLOW}██╔════╝╚══██╔══╝██╔═══██╗██╔════╝██║ ██╔╝    
{Fore.GREEN}███████╗   ██║   ██║   ██║██║     █████╔╝     
{Fore.BLUE}╚════██║   ██║   ██║   ██║██║     ██╔═██╗     
{Fore.MAGENTA}███████║   ██║   ╚██████╔╝╚██████╗██║  ██╗    
{Fore.CYAN}╚══════╝   ╚═╝    ╚═════╝  ╚═════╝╚═╝  ╚═╝    

{Fore.RED}██╗  ██╗██╗   ██╗███╗   ██╗████████╗███████╗██████╗ 
{Fore.YELLOW}██║  ██║██║   ██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗
{Fore.GREEN}███████║██║   ██║██╔██╗ ██║   ██║   █████╗  ██████╔╝
{Fore.BLUE}██╔══██║██║   ██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗
{Fore.MAGENTA}██║  ██║╚██████╔╝██║ ╚████║   ██║   ███████╗██║  ██║
{Fore.CYAN}╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝

{Fore.CYAN}║                                                                               ║
{Fore.CYAN}╚═══════════════════════════════════════════════════════════════════════════════╝"""

    print(banner)
    print(
        f"{Fore.WHITE}{Back.BLUE}                            🚀 STOCK HUNTER v2.0 🚀                           {Style.RESET_ALL}")
    print(f"{Fore.CYAN}═══════════════════════════════════════════════════════════════════════════════")
    print(f"{Fore.YELLOW}🔥 {Style.BRIGHT}Developed by {Fore.GREEN}ozcanpng{Fore.YELLOW} 🔥")
    print(f"{Fore.BLUE}🌐 GitHub: {Fore.CYAN}{Style.BRIGHT}https://github.com/ozcanpng")
    print(f"{Fore.MAGENTA}📱 Multi-Brand Stock Tracker & Notifier")
    print(f"{Fore.CYAN}═══════════════════════════════════════════════════════════════════════════════")
    print(
        f"{Fore.WHITE}🎯 {Style.BRIGHT}Desteklenen Markalar: {Fore.RED}ZARA {Fore.WHITE}| {Fore.GREEN}PULL&BEAR {Fore.WHITE}| {Fore.BLUE}BERSHKA{Style.RESET_ALL}")
    print(f"{Fore.CYAN}═══════════════════════════════════════════════════════════════════════════════\n")


def print_loading_animation():
    """Yükleme animasyonu"""
    chars = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
    for i in range(20):
        print(f"\r{Fore.CYAN}⚡ Sistem başlatılıyor... {chars[i % len(chars)]}", end="", flush=True)
        time.sleep(0.1)
    print(f"\r{Fore.GREEN}✅ Sistem başarıyla yüklendi!{' ' * 20}")


def get_all_products():
    print(
        f"\n{Fore.YELLOW}{Back.BLACK}                         📋 ÜRÜN GİRİŞ PANELİ                          {Style.RESET_ALL}")
    print(f"{Fore.CYAN}╭─────────────────────────────────────────────────────────────────────────────╮")
    print(
        f"{Fore.CYAN}│ {Fore.WHITE}Format: {Fore.GREEN}URL, BEDEN {Fore.CYAN}(örn: https://zara.com/product, M)          │")
    print(f"{Fore.CYAN}│ {Fore.WHITE}Bitirmek için: {Fore.YELLOW}Boş satır bırakın                               │")
    print(f"{Fore.CYAN}╰─────────────────────────────────────────────────────────────────────────────╯\n")

    products = []
    product_count = 1

    while True:
        line = input(f"{Fore.MAGENTA}[{product_count}] {Fore.CYAN}➤ {Fore.WHITE}").strip()
        if not line:
            break
        try:
            url, size = map(str.strip, line.split(","))
            url = url.lower()
            size = size.upper()
            products.append((url, size))
            print(f"{Fore.GREEN}   ✅ Eklendi: {Fore.BLUE}{size} {Fore.LIGHTBLACK_EX}bedeni")
            product_count += 1
        except ValueError:
            print(f"{Fore.RED}   ❌ Hatalı format! 'URL, BEDEN' şeklinde girin.")

    if products:
        print(f"\n{Fore.GREEN}🎉 Toplam {len(products)} ürün eklendi!")
        print(f"{Fore.CYAN}{'═' * 79}")

    return products


def create_tracker(driver, url, size):
    brand_colors = {
        "pullandbear": Fore.GREEN,
        "zara": Fore.RED,
        "bershka": Fore.BLUE
    }

    brand_name = ""
    color = Fore.WHITE

    if "pullandbear" in url:
        brand_name = "PULL&BEAR"
        color = brand_colors["pullandbear"]
        return PullAndBearTracker(driver, url, size)
    elif "zara" in url:
        brand_name = "ZARA"
        color = brand_colors["zara"]
        return ZaraTracker(driver, url, size)
    elif "bershka" in url:
        brand_name = "BERSHKA"
        color = brand_colors["bershka"]
        return BershkaTracker(driver, url, size)
    else:
        print(f"{Fore.RED}⚠️  Bilinmeyen marka: {url}")
        return None


def print_tracking_header():
    print(
        f"\n{Fore.WHITE}{Back.GREEN}                           🎯 STOK TAKİBİ BAŞLADI                           {Style.RESET_ALL}")
    print(f"{Fore.GREEN}╭─────────────────────────────────────────────────────────────────────────────╮")
    print(
        f"{Fore.GREEN}│ {Fore.WHITE}Takip sırasında {Fore.YELLOW}Ctrl+C {Fore.WHITE}ile çıkabilirsiniz                        │")
    print(f"{Fore.GREEN}╰─────────────────────────────────────────────────────────────────────────────╯")


def print_stock_found(info):
    print(
        f"\n{Fore.WHITE}{Back.GREEN}                            🎉 STOK BULUNDU! 🎉                            {Style.RESET_ALL}")
    print(f"{Fore.GREEN}╔═══════════════════════════════════════════════════════════════════════════════╗")
    print(f"{Fore.GREEN}║ {Fore.WHITE}✅ Beden: {Fore.YELLOW}{Style.BRIGHT}{info['size']:<20} {Fore.GREEN}║")
    print(
        f"{Fore.GREEN}║ {Fore.WHITE}🔗 URL:   {Fore.CYAN}{info['url'][:50]}{'...' if len(info['url']) > 50 else '':<20} {Fore.GREEN}║")
    print(f"{Fore.GREEN}╚═══════════════════════════════════════════════════════════════════════════════╝")


def print_checking_status(info, remaining):
    brand_emojis = {
        "zara": "🔴",
        "pullandbear": "🟢",
        "bershka": "🔵"
    }

    brand = ""
    emoji = "⚪"

    for brand_name in brand_emojis.keys():
        if brand_name in info['url']:
            brand = brand_name.upper()
            emoji = brand_emojis[brand_name]
            break

    print(
        f"{Fore.CYAN}🔍 {emoji} {brand} - {Fore.YELLOW}{info['size']} {Fore.CYAN}bedeni kontrol ediliyor... {Fore.LIGHTBLACK_EX}({remaining} ürün kaldı)")


def print_not_in_stock(info, interval):
    print(f"{Fore.RED}   ❌ Stokta yok - {Fore.YELLOW}{interval}s {Fore.RED}sonra tekrar denenecek\n")


def main():
    os.system('clear' if os.name == 'posix' else 'cls')
    print_ascii_banner()
    print_loading_animation()

    products = get_all_products()
    if not products:
        print(f"{Fore.YELLOW}⚠️  Hiç ürün girilmedi. Program sonlandırılıyor.")
        return

    interval = 5  # saniye
    print(f"\n{Fore.BLUE}🔄 Tarama aralığı: {Fore.WHITE}{interval} saniye")

    driver = setup_driver()
    print(f"{Fore.GREEN}🌐 WebDriver başlatıldı")

    trackers = []
    for url, size in products:
        tracker = create_tracker(driver, url, size)
        if tracker:
            trackers.append(tracker)

    print_tracking_header()

    try:
        cycle_count = 1
        while trackers:
            print(f"\n{Fore.MAGENTA}🔄 {Style.BRIGHT}Tarama Döngüsü #{cycle_count} {Style.RESET_ALL}")
            print(f"{Fore.CYAN}{'─' * 79}")

            for tracker in trackers[:]:  # Kopya listeyle güvenli döngü
                info = tracker.get_product_info()
                print_checking_status(info, len(trackers))

                if tracker.check_stock():
                    print_stock_found(info)
                    send_telegram_message(
                        f"🎉 STOK BULUNDU!\n\n📦 Beden: {info['size']}\n🔗 Link: {info['url']}\n\n🚀 Stock Hunter tarafından tespit edildi!")
                    trackers.remove(tracker)
                    print(f"{Fore.GREEN}✔️  {info['size']} için takip sonlandırıldı.")
                else:
                    print_not_in_stock(info, interval)

            if trackers:
                print(f"{Fore.BLUE}⏱️  {interval} saniye bekleniyor...")
                time.sleep(interval)
                cycle_count += 1
            else:
                print(
                    f"\n{Fore.GREEN}{Back.BLACK}                         🎉 TÜM STOKLAR BULUNDU! 🎉                         {Style.RESET_ALL}")

    except KeyboardInterrupt:
        print(f"\n\n{Fore.YELLOW}🛑 Takip kullanıcı tarafından sonlandırıldı.")
    finally:
        driver.quit()
        print(f"{Fore.BLUE}🔧 WebDriver kapatıldı")
        print(f"\n{Fore.CYAN}╔═══════════════════════════════════════════════════════════════════════════════╗")
        print(
            f"{Fore.CYAN}║                          {Fore.WHITE}👋 GÜLE GÜLE! {Fore.CYAN}                                     ║")
        print(f"{Fore.CYAN}║                                                                               ║")
        print(
            f"{Fore.CYAN}║           {Fore.YELLOW}Stock Hunter'ı kullandığınız için teşekkürler! {Fore.CYAN}              ║")
        print(
            f"{Fore.CYAN}║                    {Fore.GREEN}github.com/ozcanpng {Fore.CYAN}                                  ║")
        print(f"{Fore.CYAN}╚═══════════════════════════════════════════════════════════════════════════════╝")


if __name__ == "__main__":
    main()