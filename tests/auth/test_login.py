import allure
from pages.login_page import LoginPage


@allure.feature("Auth")
@allure.story("Login flow")
def test_login(page):

    login = LoginPage(page)

    login.open_login()

    login.assert_true(
        "login" in page.url or "Plane" in page.title(),
        "Login page should be opened"
    )