from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_url(self):
        assert 'basket' in self.url,  \
            f"URL:{self.url} doesn`t contain the word 'basket'"

    def should_be_message_about_empty_basket(self):
        message = self.browser.find_element(
            *BasketPageLocators.BASKET_MESSAGE
        ).text
        print(f"Message is: ///{message}///")
        assert self.is_element_present(
            *BasketPageLocators.BASKET_MESSAGE
        ),  "Message about empty basket is not presented. " \
            "Looks like products in basket"

    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(
            *BasketPageLocators.BASKET_PRODUCT
        ),  "At least one product is presented in basket."



