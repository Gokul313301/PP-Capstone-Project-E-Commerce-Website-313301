from pages.basePage import BasePage


class LoginPage(BasePage):
    def __init__(self,page):
        self.page=page
        # signupForm=page.locator('form[action="/signup"]')
        # self.nameField=signupForm.get_by_place('textbox',name='Name')
        # self.emailField=signupForm.get_by_role('textbox',name='Email Address')
        self.nameField = page.get_by_placeholder("Name")
        self.emailField = page.locator('input[data-qa="signup-email"]')
        self.signupButton=page.get_by_role("button",name="Signup")

    def navigate(self):
        self.page.goto("https://automationexercise.com/login")

    def signup(self, name, email):
        BasePage.fill(self,self.nameField,name)
        BasePage.fill(self,self.emailField,email)
        BasePage.click(self,self.signupButton)