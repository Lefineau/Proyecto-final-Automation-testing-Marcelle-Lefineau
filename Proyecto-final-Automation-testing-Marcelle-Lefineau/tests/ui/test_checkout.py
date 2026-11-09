
import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.fixture
def checkout_page(driver):

    # Iniciar sesión.
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    # Agregar producto al carrito.
    inventory = InventoryPage(driver)
    inventory.add_first_product_to_cart()
    inventory.open_cart()

    # Ingresar al checkout.
    cart = CartPage(driver)
    cart.click_checkout()

    return CheckoutPage(driver)


@pytest.mark.ui
def test_compra_exitosa(checkout_page):

    # Completar información del cliente.
    checkout_page.fill_customer_information(
        "Marcelle",
        "Lefineau",
        "1000"
    )

    # Continuar al resumen.
    checkout_page.continue_checkout()

    # Verificar que se ingresó al resumen de compra.
    assert "/checkout-step-two.html" in (
        checkout_page.driver.current_url
    ), "ERROR: No se ingresó al resumen de compra"

    # Finalizar la compra.
    checkout_page.finish_purchase()

    # Validar confirmación.
    confirmation = checkout_page.get_confirmation_message()

    assert confirmation == "Thank you for your order!", (
        "ERROR: No se confirmó la compra correctamente"
    )


@pytest.mark.ui
def test_checkout_sin_nombre(checkout_page):

    # Intentar continuar sin completar los datos.
    checkout_page.continue_checkout()

    # Obtener mensaje de error.
    error = checkout_page.get_error_message()

    assert "First Name is required" in error, (
        "ERROR: No se mostró el mensaje de nombre obligatorio"
    )
