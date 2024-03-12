import time
from urban_routes import UrbanRoutesPage
import data
from selenium import webdriver


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        options = webdriver.ChromeOptions()
        cls.driver = webdriver.Chrome(options=options)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.wait_for_page_to_load()

        routes_page.set_route(data.address_from, data.address_to)

        assert routes_page.get_from() == data.address_from
        assert routes_page.get_to() == data.address_to

    def test_set_phone(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.wait_for_page_to_load()

        routes_page.set_route(data.address_from, data.address_to)

        routes_page.click_on_ask_for_taxi_button()

        routes_page.choose_type_comfort()

        routes_page.click_on_enter_phone_number()

        routes_page.set_phone_number()

        routes_page.send_phone_code()

        routes_page.set_phone_code()

        assert routes_page.get_phone_number() == data.phone_number
        assert routes_page.get_phone_code_from_element() == routes_page.get_phone_code_received()

    def test_set_credit_card(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.wait_for_page_to_load()

        routes_page.set_route(data.address_from, data.address_to)

        routes_page.click_on_ask_for_taxi_button()

        routes_page.choose_type_comfort()

        routes_page.click_on_enter_phone_number()

        routes_page.set_phone_number()

        routes_page.send_phone_code()

        routes_page.set_phone_code()

        routes_page.confirm_code()

        routes_page.click_method_payment()

        routes_page.add_number_card()

        routes_page.set_number_card()

        routes_page.set_code_card()

        routes_page.click_out()

        assert routes_page.get_credit_card() == data.card_number
        assert routes_page.get_card_code_from_element() == data.card_code

    def test_message_for_driver(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.wait_for_page_to_load()

        routes_page.set_route(data.address_from, data.address_to)

        routes_page.click_on_ask_for_taxi_button()

        routes_page.choose_type_comfort()

        routes_page.click_on_enter_phone_number()

        routes_page.set_phone_number()

        routes_page.send_phone_code()

        routes_page.set_phone_code()

        routes_page.confirm_code()

        routes_page.click_method_payment()

        routes_page.add_number_card()

        routes_page.set_number_card()

        routes_page.set_code_card()

        routes_page.click_out()

        routes_page.clic_on_add_button()

        routes_page.button_close()

        routes_page.set_message_driver()

        assert routes_page.get_message_for_driver() == data.message_for_driver


    def test_full_flow(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.wait_for_page_to_load()

        routes_page.set_route(data.address_from, data.address_to)

        routes_page.click_on_ask_for_taxi_button()

        routes_page.choose_type_comfort()

        routes_page.click_on_enter_phone_number()

        routes_page.set_phone_number()

        routes_page.send_phone_code()

        routes_page.set_phone_code()

        routes_page.confirm_code()

        routes_page.click_method_payment()

        routes_page.add_number_card()

        routes_page.set_number_card()

        routes_page.set_code_card()

        routes_page.click_out()

        routes_page.clic_on_add_button()

        routes_page.button_close()

        routes_page.set_message_driver()

        routes_page.select_scarves()

        routes_page.select_ice_creams()

        routes_page.look_model_taxi()

        time.sleep(30)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
