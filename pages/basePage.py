class BasePage:

    def __init__(self, page):
        self.page = page

    def click(self, locator):
        self.page.locator(locator).click()

    def fill(self, locator, value):
        self.page.locator(locator).fill(value)

    def select_dropdown(self, locator, value):
        self.page.locator(locator).select_option(value)

    def check(self, locator):
        self.page.locator(locator).check()

    def get_text(self, locator):
        return self.page.locator(locator).text_content()

    def is_visible(self, locator):
        return self.page.locator(locator).is_visible()

    def navigate(self, url):
        self.page.goto(url)

        def wait_for_visible(self, locator):
            expect(
                self.page.locator(locator)
            ).to_be_visible()

    def type_text(self, locator, text):
        self.page.locator(locator).fill(text)

    def get_title(self):
        return self.page.title()

    def get_url(self):
        return self.page.url