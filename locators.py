class FormInfo:
    # data:
    form_url = 'https://dashboard.stripe.com/login'
    fake_email = 'jane_smith@gmail.com'
    fake_pass = '12345'

    # locators:
    form_container = ('xpath', '//div[contains(@class,"db-RegisterAndLoginLayout db-RegisterAndLoginLayout--login")]')
    form_header = ('xpath', '//div[@class="db-LoginTitle--v4"]/span')
    form_email = ('xpath', '//input[@id="email"]')
    form_pass = ('xpath', '//input[@id="old-password"]')
    form_checkbox = ('xpath', '//input[@id="checkbox1"]')
    form_btn = ('xpath', '//button[@data-db-analytics-name="email_password_input_sign_in_button"]')
