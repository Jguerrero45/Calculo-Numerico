import flet as ft
import time
from flet import Page, Text


def main(page: Page):
    t = Text()
    page.add(t)

    for i in range(10):
        t.value = f'step: {i}'
        page.update()
        time.sleep(1)


ft.app(target=main, view=ft.WEB_BROWSER)
