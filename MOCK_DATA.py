import re


def read_data(input_file, output_file, regex_pattern):
    with open(input_file, 'r') as file:
        data = file.read()
        matches = re.findall(regex_pattern, data)
    with open(output_file, 'w') as file:
        for match in matches:
            file.write(match + '\n')
    print(f"Данные успешно сохранены в файл {output_file}")


def show_menu():
    print("Меню:")
    print("1 - Считать имена и фамилии")
    print("2 - Считать все емайлы")
    print("3 - Считать названия файлов")
    print("4 - Считать цвета")
    print("5 - Выход")

menu_choice = 0
while menu_choice != 5:
    show_menu()
    menu_choice = int(input("Выберите опцию из меню: "))
    if menu_choice == 1:
        read_data("MOCK_DATA.txt", "names.txt", r"[A-Z][a-z]+\s[A-Z][a-z]+")
    elif menu_choice == 2:
        read_data("MOCK_DATA.txt", "emails.txt", r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b")
    elif menu_choice == 3:
        read_data("MOCK_DATA.txt", "filenames.txt", r"[A-Za-z]+\.\w+")
    elif menu_choice == 4:
        read_data("MOCK_DATA.txt", "colors.txt", r"\b#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})\b")
    elif menu_choice == 5:
        print("Выход из программы")
    else:
        print("Ошибка: выбрана неверная опция меню")
