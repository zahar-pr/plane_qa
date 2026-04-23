from pages.base_page import BasePage


class LoginPage(BasePage):

    EMAIL = "input[name='email']"
    PASSWORD = "input[name='password']"
    SUBMIT = "button[type='submit']"

    def open_login(self):
        self.log.step("Opening login page")
        self.open("https://app.plane.so/login")

    def login(self, email: str, password: str):
        self.log.step("Perform login")

        self.fill(self.EMAIL, email)
        self.fill(self.PASSWORD, password)
        self.click(self.SUBMIT)