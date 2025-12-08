def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        print("Контакт с таким именем уже существует.")
    else:
        name, phone = args
        contacts[name] = phone
        return f"Контакт {name} добавлен."

def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        name, phone = args
        contacts[name] = phone
        return f"Номер контакта {name} изменен."
    else:
        print("Контанта с таким именем нет в списке")

def func():
    print("Доступные команды: \n"
          "'hello' - старт программы\n"
          "'add [имя] [номер телефона]' - создание нового контакта\n"
          "'change [имя] [новый номер телефона]' - изменение существующего контакта \n"
          "'phone [имя]' - показать номер телефона\n"
          "'all' - показать все контакты\n"
          "'close' или 'exit' - завершение работы программы")
