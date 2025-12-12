from bot_parse import *


def main():
    contacts = {}
    print("Добро пожаловать в ассистент! (Введите 'func' для помощи)")

    while True:
        user_input = input("Введите команду: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("До свидания! Хорошего дня.")
            break

        elif command == "hello":
            print("Чем я могу вам помочь?")

        elif command == "func":
            print(get_help())

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all":
            print(get_all_contacts(contacts))

        else:
            print("Неверная команда. Введите 'func', чтобы увидеть список доступных команд.")


if __name__ == "__main__":
    main()