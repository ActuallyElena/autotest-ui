import pytest
from playwright.sync_api import sync_playwright, Page, Playwright

@pytest.fixture
def chromium_page(playwright: Playwright) -> Page:
    """Фикстура для создания новой страницы браузера."""
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    yield page

    browser.close()

@pytest.fixture(scope="session")
def initialize_browser_state() -> None:
    """
    Фикстура для регистрации нового пользователя и сохранения состояния браузера.

    Выполняет:
    - открытие браузера и регистрацию пользователя до теста;
    - сохранение состояния браузера в файл browser-state.json;
    - закрытие браузера после всех тестов.
    """
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Переход на страницу регистрации
        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        # Заполнение формы регистрации
        email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        email_input.fill('user.name@gmail.com')

        username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        username_input.fill('username')

        password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        password_input.fill('password')

        # Клик по кнопке регистрации
        registration_button = page.get_by_test_id('registration-page-registration-button')
        registration_button.click()

        # Ожидание завершения регистрации (можно заменить на ожидание конкретного элемента)
        page.wait_for_timeout(2000)

        # Дополнительная проверка: ждём появления элемента, подтверждающего регистрацию
        page.get_by_text("Welcome").wait_for(timeout=5000)  # пример

        # Сохранение состояния браузера в файл
        context.storage_state(path="browser-state.json")

        browser.close()

@pytest.fixture
def chromium_page_with_state(initialize_browser_state) -> Page:
    """
    Фикстура для создания страницы с авторизованной сессией (синхронная версия).

    Выполняет:
    - запуск браузера с использованием сохранённого состояния из browser-state.json;
    - создание новой страницы;
    - возврат объекта Page с авторизованной сессией.
    """
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state="browser-state.json")
        page = context.new_page()

        yield page

        page.close()
        context.close()
        browser.close()

