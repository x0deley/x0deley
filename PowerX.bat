@echo off
REM Установка пути к power plan
set POWER_PLAN_PATH=C:\x0deley\PowerX.pow

REM Создание power plan из бат-файла
echo [Power Plan Settings] > "%POWER_PLAN_PATH%"
echo >> "%POWER_PLAN_PATH%"
echo [Processor Power Policy] >> "%POWER_PLAN_PATH%"
echo >> "%POWER_PLAN_PATH%"
echo [Power Plan Information] >> "%POWER_PLAN_PATH%"
echo >> "%POWER_PLAN_PATH%"

REM Активация power plan
powershell -Command "Start-Process -FilePath powercfg -ArgumentList ('/import ""%POWER_PLAN_PATH%""') -Verb RunAs"
powershell -Command "Start-Process -FilePath powercfg -ArgumentList ('/setactive ""PowerX""') -Verb RunAs"

exit
