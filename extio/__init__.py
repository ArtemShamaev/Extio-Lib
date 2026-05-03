"""
extio - Расширенный ввод-вывод для консольных приложений.
"""

from ._colors import GetColors, ColorPrint
from ._keys import GetKeys
from ._waitkey import WaitKey
from ._chasters import GetChaster, PrintChaster

__all__ = [
    "GetColors",
    "ColorPrint",
    "GetKeys",
    "WaitKey",
    "GetChaster",
    "PrintChaster",
]

__version__ = "1.0.0"
