import flet as ft

def main(page: ft.Page):
    page.title = "Calculator App"
    page.window_height = 800
    page.window_width = 600
    page.window_resizable = False
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.fonts = {
        "Kanit": "https://raw.githubusercontent.com/google/fonts/master/ofl/kanit/Kanit-Regular.ttf",
        "digital": "https://raw.githubusercontent.com/google/fonts/master/ofl/digitalnumbers/DigitalNumbers-Regular.ttf",
    }

    head = ft.Text("Calculator App", size=25, text_align=ft.TextAlign.CENTER, weight=ft.FontWeight.W_900)
    result = ft.Text("0",size=40, width=350, text_align=ft.TextAlign.RIGHT, font_family="kanit")

    def display_text(e):
        data = e.control.data
        if result.value == "Error" or data == "C":
            result.value = "0"

        elif data == "Del" and len(result.value) >= 1:
            result.value = result.value[:-1]

        elif data in ("1","2","3","4","5","6","7","8","9","0","."):
            if result.value == "0":
                result.value = ""
            result.value += str(data)
        
        elif data in ("+","-","*","/","%"):
            result.value += str(data)
        
        elif data == "=":
            try:
                result.value = str(eval(result.value))
            except:
                result.value = str("Error")
        page.update()

    button_style1 = ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10), bgcolor="#efefef", color="#000000")
    button_style2 = ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10), bgcolor="#fdefc0", color="#a78227")
    button_style3 = ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10), bgcolor="#ffc33f", color="#a78227")

    row1 = ft.Row([
        ft.ElevatedButton(text="C", data="C", height=40, width=75, on_click=display_text, style=button_style2),
        ft.ElevatedButton(text="Del", data="Del", height=40, width=75, on_click=display_text, style=button_style2),
        ft.ElevatedButton(text="%", data="%", height=40, width=75, on_click=display_text, style=button_style2),
        ft.ElevatedButton(text="÷", data="/", height=40, width=75, on_click=display_text, style=button_style2),
    ],alignment=ft.MainAxisAlignment.SPACE_EVENLY)

    row2 = ft.Row([
        ft.ElevatedButton(text="7", data="7", height=40, width=75, on_click=display_text, style=button_style1),
        ft.ElevatedButton(text="8", data="8", height=40, width=75, on_click=display_text, style=button_style1),
        ft.ElevatedButton(text="9", data="9", height=40, width=75, on_click=display_text, style=button_style1),
        ft.ElevatedButton(text="x", data="*", height=40, width=75, on_click=display_text, style=button_style2),
    ],alignment=ft.MainAxisAlignment.SPACE_EVENLY)

    row3 = ft.Row([
        ft.ElevatedButton(text="4", data="4", height=40, width=75, on_click=display_text, style=button_style1),
        ft.ElevatedButton(text="5", data="5", height=40, width=75, on_click=display_text, style=button_style1),
        ft.ElevatedButton(text="6", data="6", height=40, width=75, on_click=display_text, style=button_style1),
        ft.ElevatedButton(text="+", data="+", height=40, width=75, on_click=display_text, style=button_style2),
    ],alignment=ft.MainAxisAlignment.SPACE_EVENLY)

    row4 = ft.Row([
        ft.ElevatedButton(text="1", data="1", height=40, width=75, on_click=display_text, style=button_style1),
        ft.ElevatedButton(text="2", data="2", height=40, width=75, on_click=display_text, style=button_style1),
        ft.ElevatedButton(text="3", data="3", height=40, width=75, on_click=display_text, style=button_style1),
        ft.ElevatedButton(text="-", data="-", height=40, width=75, on_click=display_text, style=button_style2),
    ],alignment=ft.MainAxisAlignment.SPACE_EVENLY)

    row5 = ft.Row([
        ft.ElevatedButton(text="0", data="0", height=40, width=160, on_click=display_text, style=button_style1),
        ft.ElevatedButton(text=".", data=".", height=40, width=75, on_click=display_text, style=button_style1),
        ft.ElevatedButton(text="=", data="=", height=40, width=75, on_click=display_text, style=button_style3),
    ],alignment=ft.MainAxisAlignment.SPACE_EVENLY)

    col = ft.Column([
        ft.Container(
            content=head,
            alignment=ft.alignment.bottom_center,
        ),
        ft.Container(
            content=result,
            padding=1,
            alignment=ft.alignment.center,
        ),
        ft.Container(
            content=row1,
            padding=1,
            alignment=ft.alignment.center,
        ),
        ft.Container(
            content=row2,
            padding=1,
            alignment=ft.alignment.center,
        ),
        ft.Container(
            content=row3,
            padding=1,
            alignment=ft.alignment.center,
        ),
        ft.Container(
            content=row4,
            padding=1,
            alignment=ft.alignment.center,
        ),
        ft.Container(
            content=row5,
            padding=1,
            alignment=ft.alignment.center,
        ),
    ],
    width=350)

    cont = ft.Container(
        content=col,
        padding=20,
        border_radius=10,
        border=ft.border.all(2, '#000000'),
    )

    page.add(
        cont,
    )

ft.app(target=main)
