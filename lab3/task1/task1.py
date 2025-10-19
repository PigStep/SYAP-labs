import os

# 1. Создать программный файл F1 в текстовом формате, записать в него
# построчно данные, вводимые пользователем. Об окончании ввода данных
# будет свидетельствовать пустая строка. Скопировать в файл F2 только
# четные строки из F1. Подсчитать размер файлов F1 и F2 (в байтах). – 3 балла

# Путь файла F1
F1_FILE_PATH = r"lab3/task1/F1.txt"
# Путь файла F2
F2_FILE_PATH = r"lab3/task1/F2.txt"


# ===== write_input_in_file =====
def _get_input():
    user_input = input("Введите строку для записи: ")
    if user_input == "":
        return None
    return user_input


def write_input_in_file(file_name):
    with open(file_name, "w") as file:
        input = _get_input()
        while input:
            file.write(input + "\n")
            input = _get_input()

    print("Обнаружена пустая строка, завершение записи")


# ===== write_even_lines_in_file =====
def _get_even_lines(f1_file_path):
    with open(f1_file_path, "r") as file:
        lines = file.readlines()
        even_lines = [line for index, line in enumerate(lines) if (index + 1) % 2 == 0]
        return even_lines


def write_even_lines_in_file(f1_file_path, f2_file_path):
    lines = _get_even_lines(f1_file_path)

    with open(f2_file_path, "w") as file:
        for line in lines:
            file.write(line)

    print("Файл F2 создан")


def _count_bytes(file_path):
    with open(file_path, "rb") as file:
        file.seek(os.SEEK_SET, os.SEEK_END)
        return file.tell()


if __name__ == "__main__":
    write_input_in_file(F1_FILE_PATH)
    write_even_lines_in_file(F1_FILE_PATH, F2_FILE_PATH)

    print(f"Размер файла F1: {_count_bytes(F1_FILE_PATH)} байт")
    print(f"Размер файла F2: {_count_bytes(F2_FILE_PATH)} байт")
