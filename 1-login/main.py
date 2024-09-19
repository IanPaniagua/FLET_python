import flet as ft
from flet import TextField, Checkbox, ElevatedButton, Text, Row, Column
from flet_core.control_event import ControlEvent

def main(page: ft.Page) -> None:
    # Set up the page title and alignment
    page.title = 'Signup'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    # Configure the window properties
    page.window.width = 400
    page.window.height = 400
    page.window.resizable = False

    # Set up form fields
    text_username: TextField = TextField(label='Username', text_align=ft.TextAlign.LEFT, width=200)
    text_password: TextField = TextField(label='Password', text_align=ft.TextAlign.LEFT, width=200, password=True)
    checkbox_signup: Checkbox = Checkbox(label='I agree to stuff', value=False)
    button_submit: ElevatedButton = ElevatedButton(text='Sign up', width=200, disabled=True)

    def validate(e: ControlEvent) -> None:
        # Enable the button only if all fields are filled and the checkbox is checked
        if all([text_username.value, text_password.value, checkbox_signup.value]):
            button_submit.disabled = False
        else:
            button_submit.disabled = True
        page.update()

    def submit(e: ControlEvent) -> None:
        # Print the values of the fields
        print('Username: ', text_username.value)
        print('Password: ', text_password.value)

        # Clear the page and show a welcome message
        page.controls.clear()
        page.add(
            Row(
                controls=[Text(value=f'Welcome: {text_username.value}', size=20)],
                alignment=ft.MainAxisAlignment.CENTER
            )
        )

    # Assign event handlers
    checkbox_signup.on_change = validate
    text_username.on_change = validate
    text_password.on_change = validate
    button_submit.on_click = submit

    # Render the signup page
    page.add(
        Row(
            controls=[
                Column(
                    controls=[
                        text_username,
                        text_password,
                        checkbox_signup,
                        button_submit
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

if __name__ == '__main__':
    ft.app(target=main)
