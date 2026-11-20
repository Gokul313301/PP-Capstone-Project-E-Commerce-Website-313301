from pages.homePage import HomePage


def test_home_page_load(page):

    home = HomePage(page)

    home.navigate()
    print(home.get_title())
    assert "Automation Exercise" in home.get_title()