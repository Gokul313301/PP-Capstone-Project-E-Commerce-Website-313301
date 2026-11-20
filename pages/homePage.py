from pages.basePage import BasePage


class HomePage(BasePage):

    def navigate(self):
        self.page.goto("https://automationexercise.com/")

    def get_title(self):
        return self.page.title()