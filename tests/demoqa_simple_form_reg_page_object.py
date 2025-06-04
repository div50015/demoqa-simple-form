from demoqa_simple_form.pages.application import app


def test_simple_reg_form():
    # GIVEN
    app.open()
    app.panel.opet_simple_form()

    # WHEN
    app.form.fill_simple_form('Igor Deg', 'div@novoch.ru', 'Russia Novocherkassk', 'Russia Sochi')

    # THEN
    app.form.test_should_simple_form('Igor Deg', 'div@novoch.ru', 'Russia Novocherkassk', 'Russia Sochi')
