import flet as ft
from flet import Column, ElevatedButton, Page, Text, TextField


def main(page: Page):
    nombre = TextField(label='Nombre', autofocus=True)
    apellido = TextField(label='Apellido')
    col_controles = Column()

    def btn_click(event):
        col_controles.controls.append(
            Text(f'Hola, {nombre.value}, {apellido.value}'))
        nombre.value = ''
        apellido.value = ''
        page.update()
        nombre.focus()
    btn_saludar = ElevatedButton('saludar', on_click=btn_click)

    page.add(
        nombre,
        apellido,
        col_controles,
        btn_saludar
    )


ft.app(target=main)
