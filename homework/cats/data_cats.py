
def get_cats_info(path):
    cats_info = []
    try:
        with open(path, 'r', encoding='utf-8') as f:
            dict_keys = ["id", "name", "age"]
            for line in f:
                data_list = line.strip().split(',')
                if len(data_list) < 3:
                    print(f"Недостатньо даних у рядку {line.strip()}")
                    continue
                try:
                    cats_age = int(data_list[2])
                except ValueError:
                    print(f"У рядку {line.strip()} 'age' не число")
                    continue
                cats_dict = dict(zip(dict_keys, data_list))
                cats_info.append(cats_dict)
            return cats_info
    except FileNotFoundError:
        print("File not found")
