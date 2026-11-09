
import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


@pytest.fixture
def cart_with_product(driver):

    # Iniciar sesión.
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    # Agregar un producto al carrito.
    inventory_page = InventoryPage(driver)
    inventory_page.add_first_product_to_cart()

    # Abrir el carrito.
    inventory_page.open_cart()

    return CartPage(driver)


@pytest.mark.ui
def test_verificar_producto_en_carrito(cart_with_product):

    products = cart_with_product.get_product_names()

    assert "Sauce Labs Backpack" in products, (
        "ERROR: El producto esperado no está en el carrito"
    )


@pytest.mark.ui
def test_verificar_cantidad_productos(cart_with_product):

    products = cart_with_product.get_cart_items()

    assert len(products) == 1, (
        f"ERROR: Se esperaba 1 producto, se encontraron {len(products)}"
    )


@pytest.mark.ui
def test_eliminar_producto_del_carrito(cart_with_product):

    cart_with_product.remove_first_product()

    products = cart_with_product.get_cart_items()

    assert len(products) == 0, (
        "ERROR: El carrito debería estar vacío"
    )


@pytest.mark.ui
def test_continuar_al_checkout(cart_with_product):

    cart_with_product.click_checkout()

    assert "/checkout-step-one.html" in (
        cart_with_product.driver.current_url
    ), "ERROR: No se ingresó al checkout"
