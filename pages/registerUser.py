from playwright.sync_api import expect
from pages.basePage import BasePage


class RegisterPage(BasePage):

    TITLE = "#id_gender1"
    PASSWORD = "#password"

    DAY = "#days"
    MONTH = "#months"
    YEAR = "#years"

    NEWSLETTER = "#newsletter"
    OFFERS = "#optin"

    FIRST_NAME = "#first_name"
    LAST_NAME = "#last_name"
    COMPANY = "#company"

    ADDRESS1 = "#address1"
    ADDRESS2 = "#address2"

    COUNTRY = "#country"

    STATE = "#state"
    CITY = "#city"
    ZIPCODE = "#zipcode"

    MOBILE = "#mobile_number"

    CREATE_ACCOUNT = "button[data-qa='create-account']"

    ACCOUNT_CREATED_TEXT = "Account Created!"
    CONTINUE_BUTTON = "a[data-qa='continue-button']"

    def verify_account_information_page(self):

        expect(
            self.page.get_by_text(
                "Enter Account Information"
            )
        ).to_be_visible()

    def fill_account_information(self, password):

        self.check(self.TITLE)

        self.fill(self.PASSWORD, password)

        self.select_dropdown(
            self.DAY, "10"
        )

        self.select_dropdown(
            self.MONTH, "5"
        )

        self.select_dropdown(
            self.YEAR, "1995"
        )

        self.check(self.NEWSLETTER)

        self.check(self.OFFERS)

    def fill_address_information(
            self,
            first_name,
            last_name,
            company,
            address1,
            address2,
            country,
            state,
            city,
            zipcode,
            mobile):

        self.fill(
            self.FIRST_NAME,
            first_name
        )

        self.fill(
            self.LAST_NAME,
            last_name
        )

        self.fill(
            self.COMPANY,
            company
        )

        self.fill(
            self.ADDRESS1,
            address1
        )

        self.fill(
            self.ADDRESS2,
            address2
        )

        self.select_dropdown(
            self.COUNTRY,
            country
        )

        self.fill(
            self.STATE,
            state
        )

        self.fill(
            self.CITY,
            city
        )

        self.fill(
            self.ZIPCODE,
            zipcode
        )

        self.fill(
            self.MOBILE,
            mobile
        )

    def click_create_account(self):

        self.click(
            self.CREATE_ACCOUNT
        )

    def verify_account_created(self):

        expect(
            self.page.get_by_text(
                self.ACCOUNT_CREATED_TEXT
            )
        ).to_be_visible()

    def continue_to_home(self):

        self.click(
            self.CONTINUE_BUTTON
        )