import allure
from pages.login_page import LoginPage


@allure.feature("Authentication")
@allure.story("Login flow")
def test_login_flow(browser_context):
    page = browser_context

    login = LoginPage(page)

    login.open_login()

    assert "Plane" in login.get_title()