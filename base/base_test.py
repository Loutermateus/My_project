from pages.login_page.page import LoginPage
from base_components.menu.menu import Menu
from pages.markers_page.page import MarkersPage

class BaseTest:

    def setup_method(self):
        self.login_page = LoginPage(self.driver)
        self.menu = Menu(self.driver)
        self.markers_pages = MarkersPage(self.driver)
