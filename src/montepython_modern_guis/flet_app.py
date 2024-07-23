import flet as ft


def main(page: ft.Page):
    if not page.session.contains_key("counter"):
        page.session.set("counter", 0)

    page.title = "Counter"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    out = ft.Ref[ft.Text]()

    def inc(e):
        v = page.session.get("counter") + 1
        page.session.set("counter", v)
        out.current.value = str(v)
        page.update()

    def dec(e):
        v = page.session.get("counter") - 1
        page.session.set("counter", v)
        out.current.value = str(v)
        page.update()

    page.add(ft.Row([
        ft.Text(ref=out, value="0"),
        ft.TextButton("+", on_click=inc),
        ft.TextButton("-", on_click=dec),
    ], alignment=ft.MainAxisAlignment.CENTER))


if __name__ == "__main__":
    ft.app(main)
