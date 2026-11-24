from pages.basePage import BasePage
from playwright.sync_api import expect

class HomePage(BasePage):
    
    LOGGED_IN_TEXT = "Logged in as"

    DELETE_ACCOUNT_LINK = "a[href='/delete_account']"

    ACCOUNT_DELETED_TEXT = "Account Deleted!"

    CONTINUE_BUTTON = "a[data-qa='continue-button']"


    def navigate(self):
        self.page.goto("https://automationexercise.com/")

    def get_title(self):
        return self.page.title()

    def verify_logged_in_user(self):
        expect(
            self.page.get_by_text(
                self.LOGGED_IN_TEXT
            )
        ).to_be_visible()

    def click_delete_account(self):

        self.click(
            self.DELETE_ACCOUNT_LINK
        )

    def verify_account_deleted(self):

        expect(
            self.page.get_by_text(
                self.ACCOUNT_DELETED_TEXT
            )
        ).to_be_visible()

    def click_continue(self):

        self.click(
            self.CONTINUE_BUTTON
        )