from pages.login import LoginPage
from pages.registerUser import RegisterPage
from utils.datagenerator import generate_user
from pages.homePage import HomePage



def test_register_user(page):

    user = generate_user()

    login_page = LoginPage(page)
    register_page = RegisterPage(page)
    home_page = HomePage(page)

    login_page.navigate()

    login_page.signup(
        user["name"],
        user["email"]
    )

    register_page.verify_account_information_page()

    register_page.fill_account_information(
        user["password"]
    )

    register_page.fill_address_information(
        user["first_name"],
        user["last_name"],
        user["company"],
        user["address1"],
        user["address2"],
        user["country"],
        user["state"],
        user["city"],
        user["zipcode"],
        user["mobile"]
    )

    register_page.click_create_account()

        # Verify Account Created
    register_page.verify_account_created()

    # Continue
    register_page.continue_to_home()

    # Verify Logged in User
    home_page.verify_logged_in_user()

    # Delete Account
    home_page.click_delete_account()

    # Verify Account Deleted
    home_page.verify_account_deleted()

    # Continue
    home_page.click_continue()