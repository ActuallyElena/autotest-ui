from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на страницу входа
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Проверяем, что кнопка Registration не активна
    registration_button = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button).to_be_disabled()

    # Заполняем поле email
    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.focus()

    for char in "user.name@gmail.com":
        page.keyboard.type(char, delay=300)

    # Заполняем поле username
    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.focus()

    for char in "username":
        page.keyboard.type(char, delay=300)

    # Заполняем поле пароль
    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.focus()

    for char in "password":
        page.keyboard.type(char, delay=300)

    # Проверяем, что кнопка Registration стала активна
    registration_button = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button).not_to_be_disabled()

    page.wait_for_timeout(5000)