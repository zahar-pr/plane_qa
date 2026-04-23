from playwright.sync_api import Page
from utils.logger import Logger
import allure


class BasePage:

    def __init__(self, page: Page):
        self.page = page
        self.log = Logger()

    def open(self, url: str):
        self.log.step(f"Opening URL: {url}")
        with allure.step(f"Open {url}"):
            self.page.goto(url, wait_until="networkidle")

    def click(self, selector: str):
        self.log.step(f"Click: {selector}")
        with allure.step(f"Click {selector}"):
            self.page.click(selector)

    def fill(self, selector: str, value: str):
        self.log.step(f"Fill {selector} = {value}")
        with allure.step(f"Fill field {selector}"):
            self.page.fill(selector, value)

    def get_title(self):
        title = self.page.title()
        self.log.info(f"Page title: {title}")
        return title

    def screenshot(self, name="screen.png"):
        self.log.info("Taking screenshot")
        self.page.screenshot(path=name)
        allure.attach.file(name, name=name, attachment_type=allure.attachment_type.PNG)