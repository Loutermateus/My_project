from base.base_test import BaseTest
import time




class TestExe(BaseTest):


    def test_login(self):
        self.login_page.open()
        self.login_page.login()
        time.sleep(3)

    def test_create_marker_and_change_name_marker(self):
        self.login_page.open()
        self.login_page.login()
        self.menu.settings.open_setting_market()
        self.markers_pages.open_create()
        self.markers_pages.create.choose_enable()
        self.markers_pages.create.fill_name("denver")
        self.markers_pages.create.fill_configuration("babu")
        self.markers_pages.create.fill_market_type("Fortex")
        self.markers_pages.create.choose_save_to_csv_file()
        self.markers_pages.create.choose_save_to_log_file()
        self.markers_pages.create.click_create()
        self.markers_pages.refresh_page()
        self.markers_pages.find_row_by_username("denver")
        self.markers_pages.click_edit_row_by_username("denver")
        self.markers_pages.edit.fill_default_configuration()
        self.markers_pages.edit.click_yes()
        self.markers_pages.edit.fill_configuration("OneZero")
        self.markers_pages.edit.fill_name("pagoda")
        time.sleep(1)
        self.markers_pages.edit.find_save()
        self.markers_pages.edit.click_save()
        self.markers_pages.refresh_page()
        self.markers_pages.find_row_by_username("pagoda")



    def test_open_and_adjust_position(self):
        self.login_page.open()
        self.login_page.login()
        self.menu.settings.open_setting_market()
        self.markers_pages.open_action_position_by_name("pagoda")
        self.markers_pages.positions.open_adjust()
        self.markers_pages.positions.adjust.fill_symbol("EUR/USD$")
        self.markers_pages.positions.adjust.fill_price("200")
        self.markers_pages.positions.adjust.fill_volume("100")
        self.markers_pages.positions.adjust.fill_comments("basta")
        self.markers_pages.positions.adjust.click_buy()
        self.markers_pages.positions.adjust.click_ok()
        self.markers_pages.refresh_page()
        self.markers_pages.open_action_position_by_name("pagoda")
        self.markers_pages.positions.find_row_by_username("EUR/USD$")
        self.markers_pages.positions.open_adjust()
        self.markers_pages.positions.adjust.fill_symbol("EUR/USD$")
        self.markers_pages.positions.adjust.fill_price("200")
        self.markers_pages.positions.adjust.fill_volume("100")
        self.markers_pages.positions.adjust.fill_comments("basta")
        self.markers_pages.positions.adjust.click_sell()
        self.markers_pages.positions.adjust.click_ok()
        self.markers_pages.refresh_page()
        self.markers_pages.open_action_position_by_name("pagoda")
        self.markers_pages.positions.cant_find_row_by_username("EUR/USD$")



    def test_set_tif_conversion(self):
        self.login_page.open()
        self.login_page.login()
        self.menu.settings.open_setting_market()
        self.markers_pages.open_create()
        self.markers_pages.create.choose_enable()
        self.markers_pages.create.fill_name("denver")
        self.markers_pages.create.fill_configuration("babu")
        self.markers_pages.create.fill_market_type("OneZero")
        self.markers_pages.create.choose_save_to_csv_file()
        self.markers_pages.create.choose_save_to_log_file()
        self.markers_pages.create.click_create()
        self.markers_pages.refresh_page()
        self.markers_pages.find_row_by_username("denver")
        self.markers_pages.open_action_tif_conversion_by_name("denver")
        self.markers_pages.tif_conversion.click_select_fok_to_gtc_checkbox_by_username("support-barto-hub")
        self.markers_pages.tif_conversion.click_select_fok_to_gtc_checkbox_by_username("support-barto-hub test")
        self.markers_pages.tif_conversion.click_select_ioc_to_gtc_checkbox_by_username("support-barto-mt4")
        self.markers_pages.tif_conversion.click_save_rules()
        self.markers_pages.tif_conversion.check_select_fok_to_gtc_checkbox_by_username("support-barto-hub test")
        self.markers_pages.tif_conversion.check_select_fok_to_gtc_checkbox_by_username("support-barto-hub")
        self.markers_pages.tif_conversion.check_select_ioc_to_gtc_checkbox_by_username("support-barto-mt4")
        self.markers_pages.tif_conversion.deselect_all()
        self.markers_pages.tif_conversion.click_save_rules()






