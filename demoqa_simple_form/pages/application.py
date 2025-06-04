from selene import browser
from demoqa_simple_form.pages.left_panel import LeftPanel
from demoqa_simple_form.pages.simple_form import SimpleForm


class Application:
    def __init__(self):
        self.panel = LeftPanel()
        self.form = SimpleForm()

    def open(self):
        browser.open('/')
        return self


app = Application()
