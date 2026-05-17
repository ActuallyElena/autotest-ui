from typing import Pattern
from playwright.sync_api import Page
from components.base_component import BaseComponent
from elements.icon import Icon
from elements.button import Button
from elements.text import Text

class SidebarListItemComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.identifier= identifier

        self.icon = Icon(
            page, '{identifier}-drawer-list-item-icon', 'Sidebar Icon'
        )
        self.title = Text(
            page, '{identifier}-drawer-list-item-title-text', 'Sidebar Title'
        )
        self.button = Button(
            page, '{identifier}-drawer-list-item-button', 'Sidebar Button'
        )

    def check_visible(self):
        self.icon.check_visible(identifier=self.identifier)
        self.title.check_visible(identifier=self.identifier)
        self.button.check_visible(identifier=self.identifier)

    def navigate(self, expected_url: Pattern[str]):
        self.button.click(identifier=self.identifier)
        self.page.wait_for_url(expected_url)

