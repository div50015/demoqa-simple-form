from selene import browser
import pytest
from time import sleep

def test_registration_simple_form():
    #GIVEN
    browser.open('https://demoqa.com/elements')
    browser.element('//*[text() = "Text Box"]').click()
    browser.element('#userName').type('Igor Deg')

    pass

    # sleep(5)
    #WHENtext-box


    #THEN


