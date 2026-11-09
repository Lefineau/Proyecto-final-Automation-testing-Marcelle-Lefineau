
import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.fixture
def logged_inventory(driver):

    # Iniciar sesión.
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    # Crear la página de inventario.
    return InventoryPage(driver)


@pytest.mark.ui
def test_verificar_productos_visibles(logged_inventory):

    products = logged_inventory.get_products()

    assert len(products) > 0, (
        "ERROR: No se encontraron productos"
    )


@pytest.mark.ui
def test_verificar_nombres_productos(logged_inventory):

    product_names = logged_inventory.get_product_names()

    assert "Sauce Labs Backpack" in product_names, (
        "ERROR: No se encontró Sauce Labs Backpack"
    )


@pytest.mark.ui
def test_agregar_producto_al_carrito(logged_inventory):

    logged_inventory.add_first_product_to_cart()

    quantity = logged_inventory.get_cart_quantity()

    assert quantity == 1, (
        f"ERROR: Se esperaba 1 producto y se encontraron {quantity}"
    )


@pytest.mark.ui
def test_ordenar_productos_por_precio(logged_inventory):

    logged_inventory.sort_products("Price (low to high)")

    selected_option = logged_inventory.driver.find_element(
        *logged_inventory.SORT_CONTAINER
    ).get_attribute("value")

    assert selected_option == "lohi", (
        "ERROR: No se seleccionó el orden de menor a mayor"
    )
