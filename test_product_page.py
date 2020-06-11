import math
import pytest
import time

from .pages.product_page import ProductPage
from selenium.common.exceptions import NoAlertPresentException


# link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
# link_1 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"


# def solve_quiz_and_get_code(browser):
#     alert = browser.switch_to.alert
#     x = alert.text.split(" ")[2]
#     answer = str(math.log(abs((12 * math.sin(float(x))))))
#     alert.send_keys(answer)
#     alert.accept()
#     try:
#         alert = browser.switch_to.alert
#         alert_text = alert.text
#         print(f"Your code: {alert_text}")
#         alert.accept()
#     except NoAlertPresentException:
#         print("No second alert presented")
#
#
# @pytest.mark.parametrize(
#     'link', [
#         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#         pytest.param(
#             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#             marks=pytest.mark.xfail
#         ),
#         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
#     ]
# )
# def test_guest_can_add_product_to_basket(browser, link):
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_to_basket()
#     solve_quiz_and_get_code(browser)
#     page.should_be_add_to_basket()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/" \
           "coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/" \
           "coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/" \
           "coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_be_disappear()





