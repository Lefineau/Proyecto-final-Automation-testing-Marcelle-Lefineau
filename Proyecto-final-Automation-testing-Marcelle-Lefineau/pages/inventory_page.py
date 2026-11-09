
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class InventoryPage(BasePage):
    """
    Representa la página de inventario de SauceDemo.
    Contiene las acciones relacionadas con los productos.
    """

    # Localizadores de elementos.
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    ADD_TO_CART_BUTTONS = (
        By.CSS_SELECTOR,
        ".inventory_item button"
    )
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    SORT_CONTAINER = (By.CLASS_NAME, "product_sort_container")

    def get_products(self):
        """Obtener todos los productos visibles."""
        return self.driver.find_elements(*self.INVENTORY_ITEMS)

    def get_product_names(self):
        """Obtener los nombres de los productos."""
        return [
            product.text
            for product in self.driver.find_elements(
                *self.PRODUCT_NAMES
            )
        ]

    def add_first_product_to_cart(self):
        """Agregar el primer producto al carrito."""
        buttons = self.driver.find_elements(
            *self.ADD_TO_CART_BUTTONS
        )
        buttons[0].click()

    def get_cart_quantity(self):
        """Consultar la cantidad de productos del carrito."""
        badges = self.driver.find_elements(*self.CART_BADGE)

        if badges:
            return int(badges[0].text)

        return 0

    def open_cart(self):
        """Ingresar a la página del carrito."""
        self.click(self.CART_LINK)

    def sort_products(self, option):
        """Ordenar productos según la opción seleccionada."""
        from selenium.webdriver.support.ui import Select

        sort_element = self.wait.until(
            lambda driver: driver.find_element(
                *self.SORT_CONTAINER
            )
        )

        Select(sort_element).select_by_visible_text(option)
