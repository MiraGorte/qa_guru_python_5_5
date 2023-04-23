from selene import browser, have
import os


def test_demo_form():
    browser.open('https://demoqa.com/automation-practice-form')

    browser.element('#firstName').type('Mira')
    browser.element('#lastName').type('Gorte')
    browser.element('#userEmail').type('Mira_Gorte@gmail.com')
    browser.element('[for = gender-radio-2]').double_click()
    browser.element('#userNumber').type('9009002020')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('[value="2000"]').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('[value="8"]').click()
    browser.element('[aria-label="Choose Friday, September 8th, 2000"]').click()

    browser.element('#subjectsInput').type('Chemistry').press_enter()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('#uploadPicture').send_keys(os.getcwd() + '/resources/cat_internet.jpg')

    browser.element('#currentAddress').type('Moscow city')
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Delhi').press_enter()

    browser.element('#submit').press_enter()

    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.all('tbody tr').should(have.exact_texts(
        'Student Name Mira Gorte', 'Student Email Mira_Gorte@gmail.com', 'Gender Female', 'Mobile 9009002020',
        'Date of Birth 08 September,2000', 'Subjects Chemistry', 'Hobbies Reading', 'Picture cat_internet.jpg',
        'Address Moscow city', 'State and City NCR Delhi'))
