import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    ElementClickInterceptedException,
)
from trackers.base_tracker import BaseTracker

class ZaraTracker(BaseTracker):
    def check_stock(self) -> bool:
        self.driver.get(self.url)
        wait = WebDriverWait(self.driver, 15)
        hedef = self.target_size.upper()

        try:
            # Çerez kutusunu kapat
            try:
                print("🧁 Çerez kontrol ediliyor...")
                cookie_button = wait.until(EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
                cookie_button.click()
                print("✅ Çerez kabul edildi.")
            except TimeoutException:
                print("⏭️ Çerez kutusu görünmedi.")

            # 'EKLE' butonuna tıkla ki bedenler aktif olsun
            try:
                print("🔘 EKLE butonuna tıklanıyor...")
                add_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-qa-action='add-to-cart']")))

                # Eğer üstte overlay varsa kaldır
                overlays = self.driver.find_elements(By.CLASS_NAME, "zds-backdrop")
                if overlays:
                    print("🧼 Overlay temizleniyor...")
                    self.driver.execute_script("arguments[0].remove();", overlays[0])

                # Tıkla
                self.driver.execute_script("arguments[0].click();", add_button)
                time.sleep(1)
                print("✅ EKLE butonuna tıklandı.")
            except Exception as e:
                print(f"[⚠️] EKLE butonuna tıklanamadı: {e}")

            # Bedenler yüklenene kadar bekle
            print("👕 Bedenler yükleniyor...")
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, "size-selector-sizes")))

            time.sleep(1)
            size_elements = self.driver.find_elements(By.CLASS_NAME, "size-selector-sizes-size")

            for li in size_elements:
                try:
                    label = li.find_element(By.CSS_SELECTOR, "div[data-qa-qualifier='size-selector-sizes-size-label']").text.strip().upper()
                    clean_label = label.split("(")[0].strip()

                    button = li.find_element(By.CLASS_NAME, "size-selector-sizes-size__button")
                    action = button.get_attribute("data-qa-action")

                    # "Benzer ürünler" yazısı varsa stokta yoktur
                    try:
                        sim_text = button.find_element(By.CLASS_NAME, "size-selector-sizes-size__action").text.strip()
                        if "BENZER" in sim_text.upper():
                            print(f"[❌] {label} — BENZER ÜRÜNLER → YOK")
                            continue
                    except NoSuchElementException:
                        pass

                    status = "VAR" if action == "size-in-stock" else "YOK"
                    print(f"[🧪] {label:<15} — {status}")

                    if clean_label == hedef and action in ["size-in-stock", "size-low-on-stock"]:
                        return True

                except Exception as e:
                    print(f"[⚠️] Beden işlenemedi: {e}")
                    continue

        except Exception as e:
            print(f"[💥] Zara genel hata: {e}")
            return False

        return False

    def get_product_info(self):
        return {
            "url": self.url,
            "size": self.target_size.upper()
        }
