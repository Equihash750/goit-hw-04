from homework.salary.calculation import total_salary
from homework.cats.data_cats import get_cats_info

total, average = total_salary("homework/salary/salary.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

cats_info = get_cats_info("homework/cats/cats_info.txt")
print(cats_info)

#if __name__ == '__main__':
    #main()