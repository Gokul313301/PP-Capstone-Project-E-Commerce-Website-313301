from pages.basePage import BasePage


class LoginPage(BasePage):
    def __init__(self,page):
        self.page=page
        self.NAME_FIELD = "input[data-qa='signup-name']"
        self.EMAIL_FIELD = "input[data-qa='signup-email']"
        self.SIGNUP_BUTTON = "button[data-qa='signup-button']"
    def navigate(self):
        self.page.goto("https://automationexercise.com/login")

    def signup(self, name, email):
        self.fill(self.NAME_FIELD, name)
        self.fill(self.EMAIL_FIELD, email)
        self.click(self.SIGNUP_BUTTON)