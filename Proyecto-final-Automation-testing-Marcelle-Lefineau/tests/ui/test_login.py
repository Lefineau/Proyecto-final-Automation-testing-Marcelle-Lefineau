import pytest

from pages.login_page import LoginPage


@pytest.mark.ui
@pytest.mark.smoke
def test_login_exitoso(driver):

    # Crear el objeto de la página de login.
    login_page = LoginPage(driver)

    # Abrir SauceDemo.
    login_page.open()

    # Iniciar sesión con credenciales válidas.
    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    # Verificar que ingresamos al inventario.
    assert "/inventory.html" in driver.current_url, (
        "ERROR: No se pudo iniciar sesión correctamente"
    )

# Prueba de login parametrizada, se leen los datos en login_data.json y se ejecuta 1 prueba x c/usuario.

import json
import pytest

from pathlib import Path
from pages.login_page import LoginPage


# Ruta del archivo externo con los datos de prueba.
DATA_FILE = (
    Path(__file__).resolve().parents[2]
    / "data"
    / "login_data.json"
)


# Leer los datos desde el archivo JSON.
with open(DATA_FILE, "r", encoding="utf-8") as file:
    login_data = json.load(file)


# Parametrizar las pruebas utilizando los datos externos.
@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.parametrize(
    "test_data",
    login_data,
    ids=[data["description"] for data in login_data]
)
def test_login(driver, test_data):

    # Crear el objeto de la página de login.
    login_page = LoginPage(driver)

    # Abrir SauceDemo.
    login_page.open()

    # Ingresar las credenciales del escenario.
    login_page.login(
        test_data["username"],
        test_data["password"]
    )

    # Validar el resultado esperado.
    if test_data["expected"] == "success":

        assert "/inventory.html" in driver.current_url, (
            "ERROR: No se pudo iniciar sesión correctamente"
        )

    elif test_data["expected"] == "locked":

        error_message = login_page.get_error_message()

        assert "locked out" in error_message.lower(), (
            "ERROR: No se mostró el mensaje de usuario bloqueado"
        )

    elif test_data["expected"] == "error":

        error_message = login_page.get_error_message()

        assert "username and password do not match" in error_message.lower(), (
            "ERROR: No se mostró el mensaje de credenciales incorrectas"
        )