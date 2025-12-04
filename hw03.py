import sys
import os
from colorama import Fore, Style

if len(sys.argv) != 2:
    print(Fore.RED + "Ошибка: Необходимо указать путь к директории.")
    print("Использование: python hw03.py [путь_к_директории]")
    Style.RESET_ALL
    sys.exit(1)
root_dir = sys.argv[1]

if not os.path.isdir(root_dir):
    print(f"{Fore.RED} Ошибка:{Fore.RESET} Директория '{root_dir}' не найдена или не является директорией.")
    sys.exit(1)

print(f"📦 Структура директории: {root_dir}")

root_sep_count = root_dir.count(os.path.sep)

for root, dirs, files in os.walk(root_dir):

    level = root.count(os.path.sep) - root_sep_count

    if level > 0:
        root_indent = '    ' * level
        print(Fore.BLUE + f"{root_indent}📂 {os.path.basename(root)}/")
    content_indent = '    ' * (level + 1)

    for f in files:
        print(Fore.GREEN + f"{content_indent}📜 {f}")
