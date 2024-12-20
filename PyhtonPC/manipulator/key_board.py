import json

from config import CONFIG_PATH, CONFIG_LANG


RUS_KEYBOARD = [
    "ё1234567890"
    "йцукенгшщзхъ",
    "фывапролджэ",
    "ячсмитьбю.",
    " ",
]

ENG_KEYBOARD = [
    "`1234567890"
    "qwertyuiop[]",
    "asdfghjkl;'",
    "zxcvbnm,./",
    " ",
]

RUS_KEYS = list(''.join(RUS_KEYBOARD))
ENG_KEYS = list(''.join(ENG_KEYBOARD))

_RUS_to_ENG = dict(zip(RUS_KEYS, ENG_KEYS))
_ENG_to_RUS = dict(zip(ENG_KEYS, RUS_KEYS))

KB_CONFIG_RUS = {
    'ё': [90, 110, 135, 42],
    '1': [90, 100, 130, 45],
    '2': [90, 93, 125, 51],
    '3': [80, 85, 120, 58],
    '4': [95, 62, 120, 63],
    '5': [90, 62, 120, 73],
    '6': [80, 67, 105, 83],
    '7': [80, 67, 110, 93],
    '8': [75, 67, 110, 103],
    '9': [75, 67, 110, 109],
    '0': [90, 67, 115, 119],
    'й': [85, 105, 135, 53],
    'ц': [85, 95, 130, 58],
    'у': [100, 77, 125, 66],
    'к': [100, 67, 125, 73],
    'е': [90, 73, 121, 79],
    'н': [95, 68, 121, 89],
    'г': [95, 66, 119, 95],
    'ш': [90, 66, 119, 105],
    'щ': [90, 71, 121, 111],
    'з': [100, 71, 121, 118],
    'х': [101, 76, 126, 125],
    'ъ': [91, 91, 128, 129],
    'ф': [95, 100, 140, 58],
    'ы': [89, 101, 134, 62],
    'в': [94, 94, 135, 69],
    'а': [100, 82, 130, 75],
    'п': [90, 94, 130, 80],
    'р': [80, 92, 130, 88],
    'о': [90, 76, 129, 95],
    'л': [97, 76, 129, 104],
    'д': [95, 76, 129, 109],
    'ж': [95, 91, 129, 116],
    'э': [90, 91, 131, 123],
    'я': [90, 120, 155, 63],
    'ч': [90, 110, 145, 68],
    'с': [90, 102, 140, 73],
    'м': [100, 102, 140, 80],
    'и': [90, 104, 140, 86],
    'т': [87, 104, 140, 91],
    'ь': [89, 86, 139, 97],
    'б': [91, 86, 138, 105],
    'ю': [91, 86, 138, 110],
    '.': [91, 91, 141, 117],
    ' ': [90, 145, 162, 82]
}
KB_CONFIG_ENG = dict()

if CONFIG_PATH:
    if CONFIG_LANG == 'RUS':
        KB_CONFIG_RUS = json.load(open(CONFIG_PATH, 'r', encoding='utf-8'))
        KB_CONFIG_ENG = {_RUS_to_ENG[key]: val for key, val in KB_CONFIG_RUS.items()}
    else:
        KB_CONFIG_ENG = json.load(open(CONFIG_PATH, 'r', encoding='utf-8'))
        KB_CONFIG_RUS = {_ENG_to_RUS[key]: val for key, val in KB_CONFIG_ENG.items()}


if __name__ == "__main__":
    print(''.join(RUS_KEYS))
    print(''.join(ENG_KEYS))

    with open('config/kb_config_eng-1.json', 'w', encoding='utf-8') as file:
        json.dump(KB_CONFIG_ENG, file, ensure_ascii=False, indent=4)
