"""Модуль ожидания нажатия заданной клавиши."""

import sys
import os
import string
from ._keys import SPECIAL_KEYS, LETTERS, UPPER_LETTERS

# --------------------------------------------------
# КАРТЫ КЛАВИШ ДЛЯ WINDOWS
# --------------------------------------------------
_WIN_KEY_MAP = {
    # Буквы (генерируем автоматически)
    **{chr(i): chr(i).encode() for i in range(ord('a'), ord('z')+1)},
    **{chr(i): chr(i).encode() for i in range(ord('A'), ord('Z')+1)},
    # Цифры
    **{str(i): str(i).encode() for i in range(10)},
    # Символы
    "/": b"/", "-": b"-", "+": b"+", "*": b"*",
    ".": b".", ",": b",", ";": b";", "'": b"'",
    "[": b"[", "]": b"]", "\\": b"\\", "`": b"`", "=": b"=",
    # Специальные
    "Any": None,
    "Tab": b"\t",
    "Return": b"\r", "Enter": b"\r",
    "Backspace": b"\x08",
    "Del": b"\xe0S", "Delete": b"\xe0S",
    "Ins": b"\xe0R", "Insert": b"\xe0R",
    "Esc": b"\x1b", "Escape": b"\x1b",
    "Space": b" ",
    # Стрелки
    "Up": b"\xe0H", "Down": b"\xe0P",
    "Left": b"\xe0K", "Right": b"\xe0M",
    # Home/End/PageUp/PageDown
    "Home": b"\xe0G", "End": b"\xe0O",
    "PageUp": b"\xe0I", "PageDown": b"\xe0Q",
    # F-клавиши
    "F1": b"\xe0;", "F2": b"\xe0<", "F3": b"\xe0=",
    "F4": b"\xe0>", "F5": b"\xe0?", "F6": b"\xe0@",
    "F7": b"\xe0A", "F8": b"\xe0B", "F9": b"\xe0C",
    "F10": b"\xe0D", "F11": b"\xe0\x85", "F12": b"\xe0\x86",
    # Модификаторы (скан-коды)
    "LShift": b"\xe0\xa0", "RShift": b"\xe0\xa1", "Shift": b"\xe0\xa0",  # Shift - любой левый
    "LCtrl": b"\xe0\xb3", "RCtrl": b"\xe0\xb4", "Ctrl": b"\xe0\xb3",    # Ctrl - любой левый
    "LAlt": b"\xe0\xb8", "RAlt": b"\xe0\xb9", "Alt": b"\xe0\xb8",       # Alt - любой левый
}

# --------------------------------------------------
# КАРТЫ КЛАВИШ ДЛЯ UNIX (Linux/macOS)
# --------------------------------------------------
_UNIX_KEY_MAP = {
    # Буквы
    **{chr(i): chr(i) for i in range(ord('a'), ord('z')+1)},
    **{chr(i): chr(i) for i in range(ord('A'), ord('Z')+1)},
    # Цифры
    **{str(i): str(i) for i in range(10)},
    # Символы
    "/": "/", "-": "-", "+": "+", "*": "*",
    ".": ".", ",": ",", ";": ";", "'": "'",
    "[": "[", "]": "]", "\\": "\\", "`": "`", "=": "=",
    # Специальные
    "Any": None,
    "Tab": "\t",
    "Return": "\n", "Enter": "\n",
    "Backspace": "\x7f",
    "Del": "\x1b[3~", "Delete": "\x1b[3~",
    "Ins": "\x1b[2~", "Insert": "\x1b[2~",
    "Esc": "\x1b", "Escape": "\x1b",
    "Space": " ",
    # Стрелки
    "Up": "\x1b[A", "Down": "\x1b[B",
    "Left": "\x1b[D", "Right": "\x1b[C",
    # Home/End/PageUp/PageDown
    "Home": "\x1b[H", "End": "\x1b[F",
    "PageUp": "\x1b[5~", "PageDown": "\x1b[6~",
    # F-клавиши
    "F1": "\x1bOP", "F2": "\x1bOQ", "F3": "\x1bOR",
    "F4": "\x1bOS", "F5": "\x1b[15~", "F6": "\x1b[17~",
    "F7": "\x1b[18~", "F8": "\x1b[19~", "F9": "\x1b[20~",
    "F10": "\x1b[21~", "F11": "\x1b[23~", "F12": "\x1b[24~",
    # Модификаторы (в терминале сложно отловить отдельно левый/правый,
    # но попробуем через разные последовательности)
    "LShift": "\x1b[2;2~", "RShift": "\x1b[2;3~", "Shift": "\x1b[2;2~",
    "LCtrl": "\x1b[2;5~", "RCtrl": "\x1b[2;6~", "Ctrl": "\x1b[2;5~",
    "LAlt": "\x1b[2;7~", "RAlt": "\x1b[2;8~", "Alt": "\x1b[2;7~",
}


def WaitKey(key_name: str):
    """Блокирует выполнение, пока не будет нажата указанная клавиша.

    Args:
        key_name: Название клавиши ('Any' для любой, 'a'-'z', 'A'-'Z', специальные).
    """
    # Для "Any" и букв/цифр — всегда разрешено
    all_letters = set(LETTERS + UPPER_LETTERS)
    if key_name not in SPECIAL_KEYS and key_name not in all_letters and key_name != "Any":
        print(f"[extio] Неизвестная клавиша '{key_name}'.")
        return

    if sys.platform == "win32":
        _waitkey_windows(key_name)
    else:
        _waitkey_unix(key_name)


def _waitkey_windows(key_name: str):
    import msvcrt

    while True:
        ch = msvcrt.getch()

        # Расширенные клавиши (стрелки, F1-F12 и т.д.)
        if ch in (b'\xe0', b'\x00'):
            ch2 = msvcrt.getch()
            # Ctrl+буква даёт код b'\x00' + буква
            if ch == b'\x00':
                # Например, Ctrl+C -> b'\x00' + b'\x63'
                ch = b'\x00' + ch2
            else:
                ch = b'\xe0' + ch2

        # Для отладки (можно раскомментировать)
        # print(f"DEBUG: {ch!r} (hex: {ch.hex() if isinstance(ch, bytes) else ''})")

        matched = False
        if key_name == "Any":
            matched = True
        else:
            expected = _WIN_KEY_MAP.get(key_name)
            if expected is not None and ch == expected:
                matched = True
            # Дополнительно: если ждём букву, проверяем оба регистра
            elif key_name in LETTERS + UPPER_LETTERS:
                if ch == key_name.encode():
                    matched = True

        if matched:
            return


def _waitkey_unix(key_name: str):
    import termios
    import tty

    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        while True:
            seq = os.read(fd, 6)
            seq_str = seq.decode("utf-8", errors="replace")

            # Для отладки
            # print(f"DEBUG: {seq_str!r}")

            matched = False
            if key_name == "Any":
                matched = True
            else:
                expected = _UNIX_KEY_MAP.get(key_name)
                if expected is not None:
                    if seq_str == expected:
                        matched = True
                    # Особые случаи
                    elif key_name in ("Return", "Enter") and seq_str in ("\n", "\r"):
                        matched = True
                    elif key_name == "Backspace" and seq_str in ("\x7f", "\x08"):
                        matched = True
                    elif key_name == "Tab" and seq_str == "\t":
                        matched = True
                    elif key_name == "Space" and seq_str == " ":
                        matched = True
                # Буквы: проверяем точное совпадение
                elif key_name in LETTERS + UPPER_LETTERS:
                    if seq_str == key_name:
                        matched = True

            if matched:
                return
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
