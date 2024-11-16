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
    'ё': [90, 90, 90, 90],
    '1': [90, 90, 90, 90],
    '2': [90, 90, 90, 90],
    '3': [90, 90, 90, 90],
    '4': [90, 90, 90, 90],
    '5': [90, 90, 90, 90],
    '6': [90, 90, 90, 90],
    '7': [90, 90, 90, 90],
    '8': [90, 90, 90, 90],
    '9': [90, 90, 90, 90],
    '0': [90, 90, 90, 90],
    'й': [90, 90, 90, 90],
    'ц': [90, 90, 90, 90],
    'у': [90, 90, 90, 90],
    'к': [90, 90, 90, 90],
    'е': [90, 73, 125, 88],
    'н': [90, 90, 90, 90],
    'г': [90, 90, 90, 90],
    'ш': [90, 90, 90, 90],
    'щ': [90, 90, 90, 90],
    'з': [90, 90, 90, 90],
    'х': [90, 90, 90, 90],
    'ъ': [90, 90, 90, 90],
    'ф': [90, 90, 90, 90],
    'ы': [90, 90, 90, 90],
    'в': [94, 94, 135, 69],
    'а': [90, 90, 90, 90],
    'п': [90, 94, 130, 80],
    'р': [80, 92, 130, 88],
    'о': [90, 90, 90, 90],
    'л': [90, 90, 90, 90],
    'д': [90, 90, 90, 90],
    'ж': [90, 90, 90, 90],
    'э': [90, 90, 90, 90],
    'я': [90, 90, 90, 90],
    'ч': [90, 90, 90, 90],
    'с': [90, 90, 90, 90],
    'м': [90, 90, 90, 90],
    'и': [90, 104, 140, 86],
    'т': [87, 104, 140, 91],
    'ь': [90, 90, 90, 90],
    'б': [90, 90, 90, 90],
    'ю': [90, 90, 90, 90],
    '.': [90, 90, 90, 90],
    ' ': [90, 90, 90, 90]
}

KB_CONFIG_ENG = {
    '`': [90, 90, 90, 90],
    '1': [90, 90, 90, 90],
    '2': [90, 90, 90, 90],
    '3': [90, 90, 90, 90],
    '4': [90, 90, 90, 90],
    '5': [90, 90, 90, 90],
    '6': [90, 90, 90, 90],
    '7': [90, 90, 90, 90],
    '8': [90, 90, 90, 90],
    '9': [90, 90, 90, 90],
    '0': [90, 90, 90, 90],
    'q': [90, 90, 90, 90],
    'w': [90, 90, 90, 90],
    'e': [90, 90, 90, 90],
    'r': [90, 90, 90, 90],
    't': [90, 90, 90, 90],
    'y': [90, 90, 90, 90],
    'u': [90, 90, 90, 90],
    'i': [90, 90, 90, 90],
    'o': [90, 90, 90, 90],
    'p': [90, 90, 90, 90],
    '[': [90, 90, 90, 90],
    ']': [90, 90, 90, 90],
    'a': [90, 90, 90, 90],
    's': [90, 90, 90, 90],
    'd': [90, 90, 90, 90],
    'f': [90, 90, 90, 90],
    'g': [90, 90, 90, 90],
    'h': [90, 90, 90, 90],
    'j': [90, 90, 90, 90],
    'k': [90, 90, 90, 90],
    'l': [90, 90, 90, 90],
    ';': [90, 90, 90, 90],
    "'": [90, 90, 90, 90],
    'z': [90, 90, 90, 90],
    'x': [90, 90, 90, 90],
    'c': [90, 90, 90, 90],
    'v': [90, 90, 90, 90],
    'b': [90, 90, 90, 90],
    'n': [90, 90, 90, 90],
    'm': [90, 90, 90, 90],
    ',': [90, 90, 90, 90],
    '.': [90, 90, 90, 90],
    '/': [90, 90, 90, 90],
    ' ': [90, 90, 90, 90]
}
