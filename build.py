# -*- coding: utf-8 -*-
import PyInstaller.__main__

# Задаем параметры PyInstaller
pyinstaller_options = [
    "--onefile",
    "--noconsole",  # Если вы хотите скрыть консольное окно (необязательно)
    "main.py",  # Замените на имя вашего основного файла
]

# Запускаем PyInstaller
PyInstaller.__main__.run(pyinstaller_options)
