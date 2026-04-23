from pages.base_page import BasePage


class WorkspacePage(BasePage):

    def is_loaded(self):
        return "workspace" in self.page.url or "project" in self.page.url