from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.config import BASE_URL


class LoginPage(BasePage):

    # Localizadores de los elementos del login.
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    ERROR_MESSAGE = (
        By.CSS_SELECTOR,
        "[data-test='error']"
    )

    # Abrir la página de SauceDemo.
    def open(self):
        self.driver.get(BASE_URL)

    # Iniciar sesión con las credenciales recibidas.
    def login(self, username, password):
        self.enter_text(self.USERNAME, username)
        self.enter_text(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

    # Obtener el mensaje de error del login.
    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)