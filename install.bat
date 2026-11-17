@echo off
setlocal enabledelayedexpansion
title Menyoo Language Packs - installer
mode con: cols=90 lines=30

set "GAME=%~1"
if not "%GAME%"=="" goto have_path

echo.
echo   Menyoo Language Packs - installer
echo   --------------------------------
echo.
echo   Drag your GTA V folder onto install.bat, or type its path here.
echo   That is the folder that contains GTA5.exe and menyooStuff.
echo.
set /p "GAME=GTA V folder: "

:have_path
set "GAME=%GAME:"=%"
set "GAME=%GAME%\"

if not exist "%GAME%menyooStuff\Language\" (
    echo.
    echo   [x] Not found: %GAME%menyooStuff\Language
    echo       Menyoo must be installed in that folder first.
    echo.
    pause
    exit /b 1
)

set "SRC=%~dp0Language"
if not exist "%SRC%\Russia.json" (
    echo.
    echo   [x] Missing Language folder next to install.bat
    echo       Keep install.bat inside the repository folder.
    echo.
    pause
    exit /b 1
)

set "BKNAME=_backup_%RANDOM%"
set "BACKUP=%GAME%menyooStuff\Language\%BKNAME%"
set "count=0"
set "backed=0"

for %%f in ("%SRC%\*.json") do (
    if exist "%GAME%menyooStuff\Language\%%~nxf" (
        if not exist "%BACKUP%" mkdir "%BACKUP%" >nul 2>&1
        copy /y "%GAME%menyooStuff\Language\%%~nxf" "%BACKUP%\" >nul 2>&1
        set /a backed+=1
    )
    copy /y "%%f" "%GAME%menyooStuff\Language\" >nul 2>&1
    if not errorlevel 1 set /a count+=1
)

echo.
echo   [ok] Installed !count! language pack^(s^) into:
echo        %GAME%menyooStuff\Language
if !backed! GTR 0 echo   [ok] !backed! existing file^(s^) saved to %BKNAME% ^(same folder^)
echo.
echo   In game:
echo     1^) Settings -^> Language -^> pick your language
echo     2^) Settings -^> Reload Language Files
echo     3^) square glyphs? Settings -^> Menu Fonts -^> Normalish
echo.
pause
