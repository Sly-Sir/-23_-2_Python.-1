# TODO Напишите функцию find_common_participants

def find_common_participants(str_1, str_2, separator=","):  # Функция принимающая две строки и разделитель
    participants_1 = set(str_1.split(separator))
    participants_2 = set(str_2.split(separator))
    common_participants = sorted(participants_1.intersection(participants_2))
    return common_participants  # Возвращение общих участников среди групп

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

print(find_common_participants(participants_first_group, participants_second_group, "|"))

