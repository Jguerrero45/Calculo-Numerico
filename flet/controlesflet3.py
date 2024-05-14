import flet as ft
from flet import Page, Text, Row


def main(page: Page):
    page.title = 'Controles 3 flet'
    row_datos = Row(controls=[Text('Python'), Text('Java'), Text('C++')])
    page.add(row_datos)


ft.app(target=main)
