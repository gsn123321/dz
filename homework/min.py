import console_ui

def main():
    console_ui.draw_header("Ласкаво просимо в гру")

    options = [
        "Почати гру",
        "Налаштування",
        "Вийти"
    ]

    console_ui.draw_menu(options)

    choice = input("Оберіть пункт: ")

    if not choice.isdigit() or int(choice) not in range(1, len(options) + 1):
        console_ui.draw_warning("Неправильний вибір!")
    else:
        print(f"Ви обрали: {options[int(choice) - 1]}")


if __name__ == "__main__":
    main()