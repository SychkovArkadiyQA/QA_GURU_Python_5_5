from selene import browser, have, be


def     test_complete_form():
        browser.config.window_width = 1400
        browser.config.window_height = 1200
        browser.config.base_url = 'https://demoqa.com/automation-practice-form'


        browser.open('/')

        browser.element('#firstName').type('Papa').click()
        browser.element('#lastName').type('Carlo').click()
        browser.element('#userEmail').type('PapaCarlo@example.com')

        browser.element('[name=gender][value=Male]').double_click()

        browser.element('#userNumber').type('9035645454').click()

        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element('.react-datepicker__year-select').element('[value="1997"]').click()
        browser.element('.react-datepicker__month-select').click()
        browser.element('.react-datepicker__month-select').element('[value="7"]').click()
        browser.element('.react-datepicker__day--009').click()

        browser.element('#subjectsInput').type('ma').press_enter()

        browser.element('[for=hobbies-checkbox-1]').click()
        browser.element('[for=hobbies-checkbox-2]').click()
        browser.element('[for=hobbies-checkbox-3]').click()

