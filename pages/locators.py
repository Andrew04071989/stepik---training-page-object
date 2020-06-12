from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (
        By.CSS_SELECTOR,
        'span.btn-group>a'
    )
    BASKET_BUTTON_INVALID = (
        By.CSS_SELECTOR,
        'a:contains("View basket_1")'
    )


# class MainPageLocators(object):
#     LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators(object):
    ADD_TO_BASKET_BUTTON = (
        By.CSS_SELECTOR,
        'button.btn.btn-lg.btn-primary.btn-add-to-basket'
    )
    PRODUCT_NAME = (
        By.CSS_SELECTOR,
        'div.col-sm-6.product_main h1'
    )
    ADD_TO_BASKET_MESSAGE = (
        By.CSS_SELECTOR,
        'div.alertinner > strong'
    )
    PRODUCT_PRICE = (
        By.CSS_SELECTOR,
        '.col-sm-6.product_main p.price_color'
    )
    BASKET_PRICE = (
        By.CSS_SELECTOR,
        'div.alert div p strong'
    )


class BasketPageLocators(object):
    BASKET_MESSAGE = (
        By.CSS_SELECTOR,
        '#content_inner>p'
    )
    BASKET_PRODUCT = (By.CSS_SELECTOR, '#basket_formset')




