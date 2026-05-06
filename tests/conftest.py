import pytest  # Импортируем pytest
from playwright.sync_api import sync_playwright, \
    Page, Playwright  # Имопртируем класс страницы, будем использовать его для аннотации типов


@pytest.fixture  # Объявляем фикстуру, по умолчанию скоуп function, то что нам нужно
def chromium_page(playwright: Playwright) -> Page:  # Аннотируем возвращаемое фикстурой значение
        # Запускаем браузер
        browser = playwright.chromium.launch(headless=False)

        # Передаем страницу для использования в тесте
        yield browser.new_page()

        # Закрываем браузер после выполнения тестов
        browser.close()