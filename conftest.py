import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def browser_context():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        context = browser.new_context(storage_state="state.json")
        page = context.new_page()

        yield page

        browser.close()