from abc import ABC, abstractmethod

class BaseTracker(ABC):
    def __init__(self, driver, url, target_size):
        self.driver = driver
        self.url = url
        self.target_size = target_size

    @abstractmethod
    def check_stock(self) -> bool:
        pass

    @abstractmethod
    def get_product_info(self) -> dict:
        pass
