"""Тестирование всех клавиш extio"""
import extio as io

def test_colors():
    """Тест цветов"""
    io.ColorPrint("1. Тест цветов:", "blue")
    for color in io.GetColors()[:9]:
        io.ColorPrint(f"   Цвет: {color}", color)

def test_ascii():
    """Тест ASCII-арта"""
    io.ColorPrint("\n2. ASCII-арт:", "blue")
    io.PrintChaster("tux")
    io.PrintChaster("dog")

def wait_for_key(key, description=""):
    """Ожидание конкретной клавиши"""
    desc = f" ({description})" if description else ""
    io.ColorPrint(f"   Нажми '{key}'{desc} или 'q' для выхода...", "yellow")
    
    # Специальный выход
    import sys
    if sys.platform != "win32":
        # На Unix сложнее, просто ждём
        io.WaitKey(key)
    else:
        io.WaitKey(key)
    print(f"   ✓ Клавиша '{key}' нажата!")

def interactive_test():
    """Интерактивное тестирование клавиш"""
    io.ColorPrint("\n3. Интерактивный тест клавиш:", "blue")
    io.ColorPrint("   (Для выхода из каждого теста нажми 'q')\n", "sea")
    
    # Буквы
    for letter in ['a', 'z', 'm']:
        io.ColorPrint(f"\n   Тест буквы '{letter}':", "sea")
        wait_for_key(letter)
    
    # Модификаторы
    mods = ['LCtrl', 'RCtrl', 'Ctrl', 'LAlt', 'RAlt', 'Alt']
    for mod in mods:
        io.ColorPrint(f"\n   Тест модификатора '{mod}':", "sea")
        io.ColorPrint(f"   (В терминале Linux/macOS может не работать)", "red")
        wait_for_key(mod)
    
    # Специальные
    specials = ['Return', 'Tab', 'Space', 'Del', 'Backspace']
    for key in specials:
        io.ColorPrint(f"\n   Тест '{key}':", "sea")
        wait_for_key(key)
    
    # F-клавиши
    for i in range(1, 13):
        key = f"F{i}"
        io.ColorPrint(f"\n   Тест '{key}':", "sea")
        wait_for_key(key)
    
    io.ColorPrint("\n✅ Все тесты пройдены! (или ты нажимал 'q')", "green")

if __name__ == "__main__":
    test_colors()
    test_ascii()
    
    io.ColorPrint("\nЗапустить интерактивный тест? (y/n): ", "yellow")
    # Используем обычный input для согласия
    answer = input().lower()
    if answer == 'y':
        interactive_test()
    else:
        io.ColorPrint("Пропускаем интерактивный тест.", "sea")
        io.ColorPrint("Можешь протестировать вручную:", "yellow")
        io.ColorPrint(">>> io.WaitKey('a')  # ждёт букву 'a'", "white")
        io.ColorPrint(">>> io.WaitKey('LCtrl')  # ждёт левый Ctrl", "white")
        io.ColorPrint(">>> io.WaitKey('F5')  # ждёт F5", "white")
