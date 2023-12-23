@echo off
set "sourceFile=C:\x0deley\GameUserSettings.ini"
set "destinationFolder=C:\Users\atlas\AppData\Local\FortniteGame\Saved\Config\WindowsClient"
set "destinationFile=%destinationFolder%\GameUserSettings.ini"

REM Копирование файла
copy /Y "%sourceFile%" "%destinationFolder%"

REM Удаление существующего файла
del "%destinationFile%"

REM Переименование скопированного файла
ren "%destinationFolder%\GameUserSettings.ini" "GameUserSettings.ini"

echo Done.
