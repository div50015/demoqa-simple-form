from selene import browser, have, be
import pytest
from time import sleep


def test_registration_simple_form():
    # GIVEN
    browser.open('/')
    browser.element('//*[text() = "Elements"]').element('../..').click()
    browser.element('//*[text() = "Text Box"]').click()

    # WHENtext-box
    browser.element('#userName').type('Igor Deg')
    browser.element('#userEmail').type('div@novoch.ru')
    browser.element('#currentAddress').type('Russia Novocherkassk')
    browser.element('#permanentAddress').type('Russia Sochi')
    browser.element('#submit').click()

    # THEN
    browser.element('#output').all('p').should(
        have.texts(
            'Name:Igor Deg',
            'Email:div@novoch.ru',
            'Current Address :Russia Novocherkassk',
            'Permananet Address :Russia Sochi',
        )
    )
