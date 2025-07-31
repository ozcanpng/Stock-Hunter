import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from trackers.base_tracker import BaseTracker

class BershkaTracker(BaseTracker):
    def check_stock(self) -> bool:
        self.driver.get(self.url)
        wait = WebDriverWait(self.driver, 20)
        hedef = self.target_size.upper()

        try:
            # Çerez popup
            try:
                cookie_btn = wait.until(EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
                cookie_btn.click()
                print("✅ Çerez kapatıldı.")
            except TimeoutException:
                print("⏭️ Çerez çıkmadı.")

            # Butonlar görünsün
            wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button[data-qa-anchor='sizeListItem']")))

            # ⚠️ JS ile gelen güncellemelerin DOM’a yansıması için 3 sn bekle
            print("🕒 Buton durumları için bekleniyor...")
            time.sleep(3)

            size_buttons = self.driver.find_elements(By.CSS_SELECTOR, "button[data-qa-anchor='sizeListItem']")

            for btn in size_buttons:
                try:
                    label = btn.get_attribute("aria-label") or ""
                    clean_label = label.split()[0].strip().upper()

                    tabindex = btn.get_attribute("tabindex")
                    is_disabled = "is-disabled" in btn.get_attribute("class")

                    status = "YOK" if tabindex == "-1" or is_disabled else "VAR"
                    print(f"[🧪] {clean_label:<4} — {status}")

                    if clean_label == hedef and status == "VAR":
                        return True

                except Exception as e:
                    print(f"[⚠️] Buton hatası: {e}")
                    continue

        except Exception as e:
            print(f"[💥] Genel hata: {e}")
            return False

        return False

    def get_product_info(self):
        return {
            "url": self.url,
            "size": self.target_size.upper()
        }
