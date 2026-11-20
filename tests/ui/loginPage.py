from pages.login import LoginPage
from utils.datagenerator import generate_user
from playwright.sync_api import expect


def test_register_page_opens(page):

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