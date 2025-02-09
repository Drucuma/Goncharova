# TODO  Напишите функцию count_letters
def count_letters(text: str) -> dict:
    dictionary = {}
    for i in text.lower():
        if i.isalpha():
            if i in dictionary:
                dictionary[i] += 1
            else:
                dictionary[i] = 1
    return dictionary

# TODO Напишите функцию calculate_frequency
def calculate_frequency(letter_count: dict) -> dict:
    total = sum(letter_count.values())
    frequency = {}
    for letter, count in letter_count.items():
        frequency[letter] = round(count / total, 2)
    return frequency

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""
letters_count = count_letters(main_str)
frequency_calculate = calculate_frequency(letters_count)
# TODO Распечатайте в столбик букву и её частоту в тексте
for char, frequency in frequency_calculate.items():
    print(f'{char}: {frequency:.2f}')