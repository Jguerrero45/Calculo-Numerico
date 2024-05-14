import flet as ft
from flet import Page, Row, TextField, ElevatedButton


def main(page: Page):

    page.title = 'Controles 4 flet'
    filas = Row(controls=[TextField(label='Ingresa tu nombre'),
                ElevatedButton(text='Enviar mi nombre')])
    filas.alignment = 'center'
    page.add(filas)


ft.app(target=main)
