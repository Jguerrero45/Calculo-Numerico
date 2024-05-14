import flet as ft
from flet import Page, Row, TextField, ElevatedButton, SafeArea, Text


def main(page: Page):
    def saludar(event):

        page.add(SafeArea(Text((f'Hola {a.value}', text_align='center'))))

    page.title = 'Controles 4 flet'
    a = TextField(label='Ingresa tu nombre')
    b = ElevatedButton(text='Enviar mi nombre', on_click=saludar)
    filas = Row(controls=[a, b])
    filas.alignment = 'center'
    page.add(filas)


ft.app(target=main)
