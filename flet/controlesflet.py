import flet as ft


def main(page: ft.page):
    t = ft.Text(value="Hola mundo", color="blue")
    page.controls.append(t)
    page.update()


ft.app(main)
