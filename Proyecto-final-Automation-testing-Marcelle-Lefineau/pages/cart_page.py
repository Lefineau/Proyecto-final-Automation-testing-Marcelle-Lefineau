
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    """
    Representa la página del carrito de compras.
    """

    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    REMOVE_BUTTONS = (
        By.CSS_SELECTOR,
        ".cart_item button"
    )
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")

    def get_cart_items(self):
        """Obtener todos los productos del carrito."""
        return self.driver.find_elements(*self.CART_ITEMS)

    def get_product_names(self):
        """Obtener los nombres de los productos del carrito."""
        return [
            item.text
            for item in self.driver.find_elements(
                *self.PRODUCT_NAMES
            )
        ]

    def remove_first_product(self):
        """Eliminar el primer producto del carrito."""
        buttons = self.driver.find_elements(
            *self.REMOVE_BUTTONS
        )

        if buttons:
            buttons[0].click()

    def click_checkout(self):
        """Continuar al proceso de checkout."""
        self.click(self.CHECKOUT_BUTTON)

    def continue_shopping(self):
        """Volver al inventario."""
        self.click(self.CONTINUE_SHOPPING_BUTTON)
