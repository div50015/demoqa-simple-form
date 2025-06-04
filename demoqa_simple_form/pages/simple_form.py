from selene import browser, have, be


class SimpleForm:
    def __init__(self):
        self.fill_name = browser.element('#userName')
        self.fill_email = browser.element('#userEmail')
        self.fill_curr_address = browser.element('#currentAddress')
        self.fill_perm_address = browser.element('#permanentAddress')
        self.click_submit = browser.element('#submit')
        self.should_simple_form = browser.element('#output').all('p')

    def fill_simple_form(self, name, email, cur_addr, per_addr):
        self.fill_name.type(name)
        self.fill_email.type(email)
        self.fill_curr_address.type(cur_addr)
        self.fill_perm_address.type(per_addr)
        self.click_submit.click()

    def test_should_simple_form(self, name, email, cur_addr, per_addr):
        self.should_simple_form.should(
            have.texts(
                f'Name:{name}',
                f'Email:{email}',
                f'Current Address :{cur_addr}',
                f'Permananet Address :{per_addr}',
            )
        )
