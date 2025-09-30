import flet as ft
import random

def main(page: ft.Page):
    page.title = "Угадай число от 1 до 100"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.padding = 20

    secret_number = random.randint(1, 100)
    attempts = 0

    title = ft.Text("Угадай число от 1 до 100!", size=24, weight=ft.FontWeight.BOLD)
    hint = ft.Text("Введи число и нажми 'Проверить'", size=16, color="blue700")
    input_field = ft.TextField(
        label="Твоё число",
        width=150,
        text_align=ft.TextAlign.CENTER,
        input_filter=ft.NumbersOnlyInputFilter(),
        max_length=3
    )
    attempts_text = ft.Text("Попыток: 0", size=16)
    result_icon = ft.Icon(None, size=40)

    def check_guess(e):
        nonlocal attempts, secret_number

        user_input = input_field.value
        if user_input is None or user_input.strip() == "":
            hint.value = "Пожалуйста, введи число!"
            hint.color = "red"
            page.update()
            return

        try:
            guess = int(user_input)
        except ValueError:
            hint.value = "Это не целое число!"
            hint.color = "red"
            page.update()
            return

        if guess < 1 or guess > 100:
            hint.value = "Число должно быть от 1 до 100!"
            hint.color = "red"
            page.update()
            return

        attempts += 1
        attempts_text.value = f"Попыток: {attempts}"

        if guess == secret_number:
            hint.value = "🎉 Поздравляю! Ты угадал!"
            hint.color = "green"
            result_icon.name = "check_circle"
            result_icon.color = "green"
            input_field.disabled = True
            guess_button.disabled = True
        elif guess < secret_number:
            hint.value = "Слишком мало! Попробуй больше 🔼"
            hint.color = "orange"
            result_icon.name = "arrow_upward"
            result_icon.color = "orange"
        else:
            hint.value = "Слишком много! Попробуй меньше 🔽"
            hint.color = "orange"
            result_icon.name = "arrow_downward"
            result_icon.color = "orange"

        input_field.value = ""
        page.update()

    def new_game(e):
        nonlocal secret_number, attempts
        secret_number = random.randint(1, 100)
        attempts = 0
        attempts_text.value = "Попыток: 0"
        hint.value = "Введи число и нажми 'Проверить'"
        hint.color = "blue700"
        input_field.value = ""
        input_field.disabled = False
        guess_button.disabled = False
        result_icon.name = None
        page.update()

    guess_button = ft.ElevatedButton("Проверить", on_click=check_guess)
    new_game_button = ft.OutlinedButton("Новая игра", on_click=new_game)

    page.add(
        ft.Column(
            controls=[
                title,
                ft.Row([result_icon], alignment=ft.MainAxisAlignment.CENTER),
                hint,
                ft.Row([input_field, guess_button], alignment=ft.MainAxisAlignment.CENTER),
                attempts_text,
                new_game_button,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
    )

ft.app(target=main, view=ft.AppView.WEB_BROWSER)