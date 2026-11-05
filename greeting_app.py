
import flet as ft


def main(page: ft.Page):
    page.title = "Greeting App"

    # TextField for entering the user's name
    name_field = ft.TextField(
        label="Enter your name",
        width=300
    )

    # Text control for displaying the greeting
    greeting = ft.Text(
        value="",
        size=20
    )

    # Function that runs when the button is clicked
    def greet_user(e):
        name = name_field.value
        greeting.value = f"Hello, {name}!"
        page.update()

    # Create the Greet Me button
    greet_button = ft.Button(
        content="Greet Me",
        on_click=greet_user
    )

    # Arrange controls vertically
    page.add(
        ft.Column(
            controls=[
                name_field,
                greet_button,
                greeting
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
    )


ft.run(main)
