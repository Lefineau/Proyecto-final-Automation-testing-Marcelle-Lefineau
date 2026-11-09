from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Buscar un elemento y esperar hasta que sea visible.
    def find_element(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    # Hacer clic cuando el elemento esté disponible.
    def click(self, locator):
        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    # Escribir texto en un campo.
    def enter_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    # Obtener el texto de un elemento.
    def get_text(self, locator):
        return self.find_element(locator).text

    # Obtener la dirección actual del navegador.
    def get_current_url(self):
        return self.driver.current_url
    