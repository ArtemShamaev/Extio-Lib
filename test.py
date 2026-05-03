"""Тестирование всех функций extio"""
import extio as io

print("=" * 50)
io.ColorPrint("ТЕСТИРОВАНИЕ EXTIO", "yellow")
print("=" * 50)

# 1. Цвета
io.ColorPrint("1. Тест цветов:", "blue")
print(f"   Доступные цвета: {io.GetColors()}")
io.ColorPrint("   Зелёный текст", "green")
io.ColorPrint("   Красный текст", "red")
io.ColorPrint("   Синий текст", "blue")
io.ColorPrint("   Жёлтый текст", "yellow")
io.ColorPrint("   Морской текст", "sea")
io.ColorPrint("   Тёмно-синий текст", "darkblue")
io.ColorPrint("   Тёмно-зелёный текст", "darkgreen")
io.ColorPrint("   Лаймовый текст", "lime")

# 2. Клавиши
io.ColorPrint("\n2. Тест клавиш:", "blue")
print(f"   Поддерживаемые клавиши: {io.GetKeys()}")

# 3. ASCII-арт
io.ColorPrint("\n3. Тест ASCII-арта:", "blue")
print(f"   Доступные персонажи: {io.GetChaster()}\n")
io.PrintChaster("tux")
io.PrintChaster("dog")
io.PrintChaster("cat")

# 4. Интерактивный тест (закомментируй если не хочешь ждать)
io.ColorPrint("\n4. Интерактивный тест:", "yellow")
io.ColorPrint("   Нажми любую клавишу для продолжения...", "sea")
io.WaitKey("Any")
io.ColorPrint("   Клавиша нажата! Тест пройден успешно!", "green")

io.ColorPrint("\n✅ Все тесты пройдены!", "green")
