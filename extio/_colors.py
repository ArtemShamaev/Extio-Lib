"""Модуль для цветного вывода в консоль."""

import sys

# ANSI-коды цветов
COLORS = {
    "green": "32",
    "blue": "34",
    "red": "31",
    "yellow": "33",
    "sea": "36",        # cyan
    "darkblue": "34;1", # ярко-синий
    "darkgreen": "32;1",
    "lime": "92",
    "white": "37",
}

# Авто-определение поддержки цветов
if sys.platform == "win32":
    try:
        import ctypes
        kernel32 = ctypes.windll.kernel32
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
    except Exception:
        pass


def GetColors():
    """Возвращает список всех поддерживаемых цветов."""
    return list(COLORS.keys())


def ColorPrint(text: str, color: str):
    """Печатает текст заданным цветом.

    Args:
        text: Текст для вывода.
        color: Название цвета (см. GetColors()).
    """
    color = color.lower()
    code = COLORS.get(color)
    if code is None:
        print(f"[extio] Цвет '{color}' не поддерживается. Доступны: {GetColors()}")
        print(text)
        return
    print(f"\033[{code}m{text}\033[0m")
