from selene import browser, have, be


def     test_complete_form():
        browser.config.window_width = 1400
        browser.config.window_height = 1200
        browser.config.base_url = 'https://demoqa.com/automation-practice-form'


        browser.open('/')

        browser.element('#firstName').type('Papa').click()
        browser.element('#lastName').type('Carlo').click()
        browser.element('#userEmail').type('PapaCarlo@example.com')