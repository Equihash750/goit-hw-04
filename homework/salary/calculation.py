
def total_salary(path):
    total = 0
    count = 0

    try:
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                data_list = line.strip().split(',')
                if len(data_list) < 2:
                    continue
                try:
                    salary = float(data_list[1])
                    total += salary
                    count += 1
                except ValueError:
                    print(f"{data_list[1]} is not a number")
            if count > 0:
                average = total / count
            else:
                average = 0
            return total, average
    except FileNotFoundError:
        print("File not found")
        return 0, 0
