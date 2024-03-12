import data
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    phone_code = None

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, address_from, address_to):
        self.set_from(address_from)
        self.set_to(address_to)

    def click_on_ask_for_taxi_button(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".button.round")))
        elm = self.driver.find_element(By.CSS_SELECTOR, ".button.round")
        elm.click()

    def choose_type_comfort(self):
        elm_comfort = self.driver.find_element(By.XPATH, '//img[@alt="Comfort"]') # Elegir tipo de comfort.
        elm_comfort.click()

    def click_on_enter_phone_number(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".np-text")))
        elm_np = self.driver.find_element(By.CSS_SELECTOR, '.np-text') # Hacer clic para colocar el número de telefono.
        elm_np.click()

    def set_phone_number(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_element_located((By.ID, "phone")))
        elm_phone = self.driver.find_element(By.ID, 'phone') #Colocar número de telefono .
        elm_phone.send_keys(data.phone_number)

    def get_phone_number(self):
        return self.driver.find_element(By.ID, 'phone').get_property('value')

    def send_phone_code(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".button.full")))
        elm_next = self.driver.find_element(By.CSS_SELECTOR, '.button.full')# Enviar código de confirmación.
        elm_next.click()

    def set_phone_code(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_element_located((By.ID, "code")))
        elm_code = self.driver.find_element(By.ID, 'code') #Colocar código de confirmación.
        self.phone_code = retrieve_phone_code(self.driver)
        elm_code.send_keys(self.phone_code)

    def get_phone_code_received(self):
        return self.phone_code

    def get_phone_code_from_element(self):
        return self.driver.find_element(By.ID, 'code').get_property('value')

    def confirm_code(self):
        elm_confirm = self.driver.find_element(By.XPATH, '//button[text()="Confirmar"]') #Confirmar código.
        elm_confirm.click()

    def click_method_payment(self):
        elm_pp_text = self.driver.find_element(By.CSS_SELECTOR, '.pp-text') #Click en método de pago.
        elm_pp_text.click()

    def add_number_card(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '.pp-checkbox')))
        elm_pp_add_card = self.driver.find_element(By.CSS_SELECTOR, '.pp-row.disabled') # click para agregar número de tarjeta.
        elm_pp_add_card.click()

    def set_number_card(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_element_located((By.ID, 'number')))
        elm_number_card = self.driver.find_element(By.ID, 'number') # Colocar número de tarjeta.
        elm_number_card.click()
        elm_number_card.send_keys(data.card_number)

    def get_credit_card(self):
        return self.driver.find_element(By.ID, 'number').get_property('value')

    def set_code_card(self):
        elm_code_card = self.driver.find_element(By.NAME, 'code') # Colocar código de tarjeta.
        elm_code_card.click()
        elm_code_card.send_keys(data.card_code)

    def get_card_code_from_element(self):
        return self.driver.find_elements(By.ID, 'code')[1].get_property('value')

    def click_out(self):
        elm_out = self.driver.find_element(By.CSS_SELECTOR, '.card-number-label') # Click afuera para activar boton agregar.
        elm_out.click()

    def clic_on_add_button(self):
        elm_add_button = self.driver.find_element(By.XPATH, '//button[text()="Agregar"]') # Click en boton agregar.
        elm_add_button.click()

    def button_close(self):
        elm_close_button = self.driver.find_elements(By.CSS_SELECTOR, '.close-button.section-close') # Click en boton cerrrar.
        elm_close_button[2].click()


    def set_message_driver(self):
        elm_message = self.driver.find_element(By.ID,'comment') # Llenar campo de comentario al conductor
        elm_message.send_keys(data.message_for_driver)

    def get_message_for_driver(self):
        return self.driver.find_element(By.ID, 'comment').get_property('value')

    def select_scarves(self):
        elm_scarves = self.driver.find_element(By.CSS_SELECTOR, '.switch') # Seleccionar pañuelos.
        elm_scarves.click()


    def select_ice_creams(self):
        elm_ice_creams= self.driver.find_element(By.CSS_SELECTOR, '.counter-plus') # Seleccionar helados.
        elm_ice_creams.click()
        elm_ice_creams.click()

    def look_model_taxi(self):
            elm_modal = self.driver.find_element(By.CSS_SELECTOR, '.smart-button') # Visualizar modal buscar taxi.
            elm_modal.click()

    def wait_for_page_to_load(self):
        # Asegurar que la página ha terminado de cargar
        WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".workflow")))