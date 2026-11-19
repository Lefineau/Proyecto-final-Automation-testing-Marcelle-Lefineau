"""Fixtures compartidas por las pruebas."""
import pytest
from selenium import webdriver

from utils.config import BROWSER
from utils.logger import get_logger

logger = get_logger(__name__)


@pytest.fixture
def driver(request):
    """Inicia y cierra una instancia nueva del navegador por prueba."""
    browser_name = BROWSER.lower()
    logger.info("Iniciando navegador: %s | prueba: %s", browser_name, request.node.nodeid)

    if browser_name == "firefox":
        browser = webdriver.Firefox()
    elif browser_name == "chrome":
        browser = webdriver.Chrome()
    else:
        raise ValueError(f"Navegador no soportado: {BROWSER}")

    request.node._screenshot_driver = browser
    browser.maximize_window()
    yield browser

    logger.info("Cerrando navegador | prueba: %s", request.node.nodeid)
    browser.quit()
