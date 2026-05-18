@echo off
chcp 65001 >nul

setlocal enabledelayedexpansion

:: Lag strengen med 67 "67"
set "tekst="
for /l %%i in (1,1,67) do (
    set "tekst=!tekst!67 "
)
set "tekst=!tekst:~0,-1!"

:: Opprett mapper i dybden der alle heter 67
for /l %%i in (1,1,67) do (
    mkdir "67"
    cd "67"
    echo !tekst! > "67.txt"
)

echo Ferdig! 67 nestede mapper med navnet 67 er opprettet.
pause