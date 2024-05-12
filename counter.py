import flet
from flet import Page, TextField, Row, IconButton, icons


def main(page: Page):
    page.title = "Contador"
    page.vertical_alignment = "center"

    txt_numer = TextField(value='0', text_align='right', width=100)

    def minus_click(event):
        if txt_numer.value > 0:
            txt_numer.value = int(txt_numer.value) - 1
            page.update()
        else:
            pass

    def plus_click(event):
        txt_numer.value = int(txt_numer.value) + 1
        page.update()

    page.add(
        Row([
            IconButton(icons.REMOVE, on_click=minus_click),
            txt_numer,
            IconButton(icons.ADD, on_click=plus_click)
        ])
    )


flet.app(target=main)
