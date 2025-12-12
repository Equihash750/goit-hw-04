import sys
import os
from colorama import Fore, Style

VERTICAL_LINE = "┃   "
INDENT_SPACE = "    "
BRANCH_CONTINUE = "┣━━ "
BRANCH_END = "┗━━ "


def print_tree(root_dir):
    tree_data = {}

    for root, dirs, files in os.walk(root_dir):
        dirs.sort()
        files.sort()
        tree_data[root] = {'dirs': dirs, 'files': files}

    root_sep_count = root_dir.count(os.path.sep)

    print(f"{Fore.CYAN}📦 Структура директорії: {os.path.basename(root_dir)}{Style.RESET_ALL}")

    def print_node(current_path, prefix_list):
        data = tree_data.get(current_path, {'dirs': [], 'files': []})
        dirs = data['dirs']
        files = data['files']

        all_items = dirs + files
        num_items = len(all_items)

        for i, item in enumerate(all_items):
            is_last = (i == num_items - 1)

            branch = BRANCH_END if is_last else BRANCH_CONTINUE

            indent = "".join(prefix_list)

            if item in dirs:
                print(Fore.BLUE + f"{indent}{branch}📂 {item}{Style.RESET_ALL}")

                new_prefix_item = INDENT_SPACE if is_last else VERTICAL_LINE
                new_prefix_list = prefix_list + [new_prefix_item]

                next_path = os.path.join(current_path, item)
                if next_path in tree_data:
                    print_node(next_path, new_prefix_list)

            else:
                print(Fore.GREEN + f"{indent}{branch}📜 {item}{Style.RESET_ALL}")

    print_node(root_dir, [])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(Fore.RED + "Помилка: Необхідно вказати шлях до директорії.")
        print("Використання: python <ім'я_файлу>.py [шлях_до_директорії]")
        Style.RESET_ALL
        sys.exit(1)

    root_dir = sys.argv[1]

    if not os.path.isdir(root_dir):
        print(f"{Fore.RED} Помилка:{Style.RESET_ALL} Директорія '{root_dir}' не знайдена або не є директорією.")
        sys.exit(1)

    print_tree(root_dir)