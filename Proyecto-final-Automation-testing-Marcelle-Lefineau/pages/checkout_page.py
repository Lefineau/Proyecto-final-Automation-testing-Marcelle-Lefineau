
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    """
    Representa las páginas del proceso de checkout.
    """

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    CANCEL_BUTTON = (By.ID, "cancel")
    ERROR_MESSAGE = (
        By.CSS_SELECTOR,
        "[data-test='error']"
    )
    COMPLETE_TITLE = (By.CLASS_NAME, "complete-header")

    def fill_customer_information(self, first_name, last_name, postal_code):
        """Completar los datos del cliente."""

        self.driver.find_element(*self.FIRST_NAME).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)
        self.driver.find_element(*self.POSTAL_CODE).send_keys(postal_code)

    def continue_checkout(self):
        """Continuar al resumen de compra."""
        self.click(self.CONTINUE_BUTTON)

    def finish_purchase(self):
        """Finalizar la compra."""
        self.click(self.FINISH_BUTTON)

    def get_error_message(self):
        """Obtener el mensaje de error."""
        return self.driver.find_element(
            *self.ERROR_MESSAGE
        ).text

    def get_confirmation_message(self):
        """Obtener el mensaje de confirmación."""
        return self.driver.find_element(
            *self.COMPLETE_TITLE
        ).text
