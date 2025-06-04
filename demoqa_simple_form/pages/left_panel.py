from selene import browser, have, be


class LeftPanel:
    def __init__(self):
        self.open_elements = browser.element('//*[text() = "Elements"]').element('../..')
        self.open_text_box = browser.element('//*[text() = "Text Box"]')

    def opet_simple_form(self):
        self.open_elements.click()
        self.open_text_box.click()
