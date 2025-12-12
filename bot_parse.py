def parse_input(user_input):
    if not user_input.strip():
        return "", []
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def add_contact(args, contacts):
    if len(args) < 2:
        return "Ошибка: введите имя и номер телефона."
    name, phone = args
    if name in contacts:
        return f"Контакт с именем '{name}' уже существует."
    contacts[name] = phone
    return f"Контакт '{name}' успешно добавлен."

def change_contact(args, contacts):
    if len(args) < 2:
        return "Ошибка: введите имя и новый номер телефона."
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f"Номер контакта '{name}' обновлен."
    return f"Ошибка: контакт с именем '{name}' не найден."

def show_phone(args, contacts):
    if not args:
        return "Ошибка: введите имя контакта."
    name = args[0]
    if name in contacts:
        return f"Номер телефона {name}: {contacts[name]}"
    return f"Ошибка: контакт с именем '{name}' не найден."

def get_all_contacts(contacts):
    if not contacts:
        return "Список контактов пока пуст."
    result = "Список всех контактов:\n"
    for name, phone in contacts.items():
        result += f"• {name}: {phone}\n"
    return result.strip()

def get_help():
    return (
        "Доступные команды:\n"
        "  hello       - приветствие\n"
        "  add [имя] [номер]    - сохранить новый контакт\n"
        "  change [имя] [номер] - изменить существующий номер\n"
        "  phone [имя]          - показать номер по имени\n"
        "  all         - вывести все контакты\n"
        "  exit/close  - выйти из программы"
    )