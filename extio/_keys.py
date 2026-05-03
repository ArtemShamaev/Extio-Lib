"""Модуль для перечисления поддерживаемых клавиш."""

import string

# Генерируем все буквенные клавиши
LETTERS = list(string.ascii_lowercase)  # a-z
UPPER_LETTERS = list(string.ascii_uppercase)  # A-Z

# Специальные клавиши
SPECIAL_KEYS = [
    "Any",
    "Shift", "RShift", "LShift",
    "RCtrl", "LCtrl", "Ctrl",
    "RAlt", "LAlt", "Alt",
    "Tab", "Return", "Enter",
    "Del", "Delete",
    "Backspace",
    "Ins", "Insert",
    "Esc", "Escape",
    "Space",
    "Up", "Down", "Left", "Right",
    "Home", "End", "PageUp", "PageDown",
    "F1", "F2", "F3", "F4", "F5", "F6",
    "F7", "F8", "F9", "F10", "F11", "F12",
    "/", "-", "+", "*", ".", ",", ";", "'", "[", "]", "\\", "`", "=",
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
]


def GetKeys():
    """Возвращает список строк с названиями поддерживаемых клавиш."""
    return SPECIAL_KEYS + LETTERS + UPPER_LETTERS
