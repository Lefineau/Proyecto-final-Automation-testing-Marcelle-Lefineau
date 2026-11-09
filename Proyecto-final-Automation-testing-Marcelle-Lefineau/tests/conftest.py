import pytest
from selenium import webdriver

from utils.config import BROWSER


@pytest.fixture
def driver():

    # Iniciar el navegador configurado.
    if BROWSER.lower() == "firefox":
        browser = webdriver.Firefox()

    elif BROWSER.lower() == "chrome":
        browser = webdriver.Chrome()

    else:
        raise ValueError("Navegador no soportado")

    # Maximizar la ventana.
    browser.maximize_window()

    yield browser

    # Cerrar el navegador al finalizar la prueba.
    browser.quit()