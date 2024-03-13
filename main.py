from urban_routes import UrbanRoutesPage
import data
from selenium import webdriver


class TestUrbanRoutes:

    driver = None
    routes_page = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        options = webdriver.ChromeOptions()
        cls.driver = webdriver.Chrome(options=options)
        cls.driver.get(data.urban_routes_url)
        cls.routes_page = UrbanRoutesPage(cls.driver)

    def test_set_route(self):
        self.routes_page.wait_for_page_to_load()

        self.routes_page.set_route(data.address_from, data.address_to)

        assert self.routes_page.get_from() == data.address_from
        assert self.routes_page.get_to() == data.address_to

    def test_choose_type_comfort(self):
        self.routes_page.click_on_ask_for_taxi_button()

        self.routes_page.choose_type_comfort()

        assert self.routes_page.get_type_comfort_value() == "Comfort"

    def test_set_phone(self):
        self.routes_page.click_on_enter_phone_number()

        self.routes_page.set_phone_number()

        self.routes_page.send_phone_code()

        self.routes_page.set_phone_code()

        assert self.routes_page.get_phone_number() == data.phone_number
        assert self.routes_page.get_phone_code_from_element() == self.routes_page.get_phone_code_received()

    def test_set_credit_card(self):
        self.routes_page.confirm_code()

        self.routes_page.click_method_payment()

        self.routes_page.add_number_card()

        self.routes_page.set_number_card()

        self.routes_page.set_code_card()

        self.routes_page.click_out()

        assert self.routes_page.get_credit_card() == data.card_number
        assert self.routes_page.get_card_code_from_element() == data.card_code

    def test_message_for_driver(self):
        self.routes_page.clic_on_add_button()

        self.routes_page.button_close()

        self.routes_page.set_message_driver()

        assert self.routes_page.get_message_for_driver() == data.message_for_driver

    def test_select_tissues(self):
        self.routes_page.select_tissues()

        assert self.routes_page.get_select_tissues_value() == True

    def test_select_ice_cream(self):
        self.routes_page.select_ice_creams()

        assert self.routes_page.get_select_ice_cream() == '2'

    def test_look_model_taxi(self):
        self.routes_page.look_model_taxi()

        assert self.routes_page.get_look_model_taxi() == 'order shown'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
