from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage


def test_open_and_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        login_page = LoginPage(page)

        login_page.open_login()

        assert "Plane" in login_page.get_title()

        browser.close()