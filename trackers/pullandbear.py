import time
from selenium.webdriver.common.by import By
from trackers.base_tracker import BaseTracker

class PullAndBearTracker(BaseTracker):
    def get_shadow_root(self, element):
        return self.driver.execute_script("return arguments[0].shadowRoot", element)

    def check_stock(self) -> bool:
        self.driver.get(self.url)
        time.sleep(5)

        try:
            comp_1 = self.driver.find_element(By.CSS_SELECTOR, "size-selector-with-length")
            shadow_1 = self.get_shadow_root(comp_1)
            comp_2 = shadow_1.find_element(By.CSS_SELECTOR, "size-selector-select")
            shadow_2 = self.get_shadow_root(comp_2)
            comp_3 = shadow_2.find_element(By.CSS_SELECTOR, "size-list")
            shadow_3 = self.get_shadow_root(comp_3)
            ul = shadow_3.find_element(By.CSS_SELECTOR, "ul")
            size_items = ul.find_elements(By.CSS_SELECTOR, "li")

            for item in size_items:
                full_text = item.text.upper()
                label = (full_text
                         .split("BENZER")[0]
                         .split("SON ÜRÜNLER")[0]
                         .strip())

                status = "stokta yok" if "BENZER ÜRÜNLERI" in full_text else "VAR"
                print(f"[🧪] {label:<4} — {status}")

                if label == self.target_size.upper() and status == "VAR":
                    return True
        except Exception as e:
            print(f"[💥] Selenium hatası: {e}")
            return False

        return False

    def get_product_info(self) -> dict:
        return {
            "url": self.url,
            "size": self.target_size.upper()
        }
