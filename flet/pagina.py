import flet
from flet import Page


def main(page: Page):
    Page.title = "Pagina nueva"
    page.vertical_alignment = "center"


flet.app(target=main)
