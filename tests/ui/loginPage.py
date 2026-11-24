from pages.login import LoginPage
from utils.datagenerator import generate_user
from playwright.sync_api import expect
from pages.homePage import HomePage
from tests.ui.registerUserPage import register_new_user


def verify_signup(page):

    user = generate_user()

    login = LoginPage(page)

    login.navigate()

    login.signup(
        user["name"],
        user["email"]
    )

    expect(
    page.get_by_text("Enter Account Information")
).to_be_visible()

def test_login_valid_user(page):

    login_page = LoginPage(page)
    home_page = HomePage(page)
    #create new user alone
    register_user=register_new_user(page)

    #logout the new user
    home_page.logout()

    # Navigate
    login_page.navigate()

    # Verify Login Page
    login_page.verify_login_page()
    tempEmail=login_page.loginAccounts.pop()
    # Login
    login_page.login(tempEmail,"Welcome@123")

    # Verify Login Success
    home_page.verify_logged_in_user()

    # Delete Account
    home_page.click_delete_account()

    # Verify Account Deleted
    home_page.verify_account_deleted()