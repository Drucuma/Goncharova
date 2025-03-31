# TODO Напишите функцию find_common_participants
def find_common_participants(first, second, dop=','):
    first1 = set(first.split(dop))
    second2 = set(second.split(dop))
    new1 = sorted(first1.intersection(second2))
    return new1




participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

print(find_common_participants(participants_first_group, participants_second_group, "|"))

