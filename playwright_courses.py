from playwright.sync_api import sync_playwright, expect

# Открываем браузер с использованием Playwright
with sync_playwright() as playwright:
    # Запускаем Chromium браузер в обычном режиме (не headless)
    browser = playwright.chromium.launch(headless=False)
    # Создаем новый контекст браузера (новая сессия, которая изолирована от других)
    context = browser.new_context()
    # Открываем новую страницу в рамках контекста
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('user.name@gmail.com')

    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill('username')

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill('password')

    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    # Сохраняем состояние браузера (куки и localStorage) в файл для дальнейшего использования
    context.storage_state(path="browser-state.json")
    from playwright.sync_api import sync_playwright

    # Остальной код регистрации нового пользователя без изменений

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json")  # Указываем файл с сохраненным состоянием
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    page.wait_for_timeout(5000)

    # Проверяем наличие заголовка Courses
    course_exist_alert = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(course_exist_alert).to_be_visible()
    expect(course_exist_alert).to_have_text("Courses")

    # Проверяем наличие иконки
    icon_alert = page.get_by_test_id('courses-list-empty-view-icon')
    expect(icon_alert).to_be_visible()

    # Проверяем наличие текста "There is no results"
    no_result_alert = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(no_result_alert).to_be_visible()
    expect(no_result_alert).to_have_text("There is no results")

    # Проверяем наличие текста "Results from the load test pipeline will be displayed here"
    results_alert = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(results_alert).to_be_visible()
    expect(results_alert).to_have_text("Results from the load test pipeline will be displayed here")

