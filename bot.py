from bot_parse import *

def main():
    contacts = {}
    print("Добро пожаловать! (Для получения списка доступных команд введите 'func')")
    while True:
        user_input = input("Введите вашу команду: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Досвидания")
            break

        elif command == "hello":
            print("Чем я могу вам помочь? ")
        elif command == "func":
            print(func())
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "all":
            for key, value in contacts.items():
                print(f"{key}: {value}")
        elif command == "phone":
            for key, value in contacts.items():
                if key in args:
                    print(f"{value}")
        else:
            print("Неверная команда")

if __name__ == "__main__":
    main()