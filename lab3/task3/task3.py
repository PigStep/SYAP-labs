import re

# 3. Сформировать (не программно) текстовый файл. В нём каждая
# строка должна описывать учебный предмет и наличие лекционных,
# практических и лабораторных занятий по предмету. Сюда должно входить и
# количество занятий. Необязательно, чтобы для каждого предмета были все
# типы занятий.
# Сформировать словарь, содержащий название предмета и общее
# количество занятий по нему. Вывести его на экран.
# Примеры строк файла: Информатика: Физика: 30(л) 10(лаб)
# Физика: 30(л) 10(лаб)
# Физкультура: 30(пр)
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”:
# 30}– 3 балла

# путь к файлу
SUBJECTS_FILE = r"lab3\task3\subjects.txt"


def _read_subjects(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        return file.readlines()


def _extract_total_classes(raw_classes_line):
    pattern = r"(\d+)\s*\(\w+\)"
    matches = re.findall(pattern, raw_classes_line)
    return list(map(int, matches))


def _extract_subject_and_classes(subjects_line):
    subjects = []
    for subject in subjects_line:
        subject_name, subject_classes_raw = tuple(subject.split(":"))
        subject_classes_total = _extract_total_classes(subject_classes_raw)

        subjects.append((subject_name, subject_classes_total))

    return subjects


def _get_subjects(file_name):
    subjects_line = _read_subjects(file_name)
    return _extract_subject_and_classes(subjects_line)


def return_subjects_in_dict(file_name):
    subjects = _get_subjects(file_name)
    subj_dict_total = {}

    for subject_name, subject_classes_total in subjects:
        subj_dict_total[subject_name] = sum(subject_classes_total)

    print(subj_dict_total)


if __name__ == "__main__":
    return_subjects_in_dict(SUBJECTS_FILE)
