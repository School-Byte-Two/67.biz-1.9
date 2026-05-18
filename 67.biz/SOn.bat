@echo off
color 0A
echo Starter avspilling av alle .wav-filer i mappen...

:: Går gjennom alle .wav-filer i gjeldende mappe
for %%f in (*.wav) do (
    echo Spiller av: "%%f"
    :: Spiller av lyden og venter til filen er ferdig før den går videre
    start /wait wmplayer.exe /play /close "%%f"
)

echo.
echo Avspillingen er ferdig!
pause