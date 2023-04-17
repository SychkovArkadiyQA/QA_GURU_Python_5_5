from selene import browser, have, be


def     test_complete_form():
        browser.config.window_width = 1400
        browser.config.window_height = 1200
        browser.config.base_url = 'https://demoqa.com/automation-practice-form'


        browser.open('/')

        browser.element('#firstName').type('Papa').click()
        browser.element('#lastName').type('Carlo').click()
        browser.element('#userEmail').type('PapaCarlo@example.com')

        browser.element('#gender').element('#male')

        browser.element('#userNumber').type('9035645454').click()

        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').element('#1997')
        browser.element('.react-datepicker__month-select').element('#7')
        browser.element('.react-datepicker__day--009').click()
