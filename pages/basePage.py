from playwright.sync_api import Locator


class BasePage:

    def __init__(self, page):
        self.page = page

    def click(self, locator: Locator) -> None:
        locator.click()

    def fill(self, locator: Locator, value: str) -> None:
        locator.fill(value)

    def get_text(self, locator: Locator) -> str | None:
        return locator.text_content()

    def is_visible(self, locator: Locator) -> bool:
        return locator.is_visible()