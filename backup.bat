@echo off
cd /d "%~dp0"

:: Format time correctly
set hour=%time:~0,2%
if "%hour:~0,1%"==" " set hour=0%hour:~1,1%
set timestamp=%date:~10,4%-%date:~4,2%-%date:~7,2%_%hour%-%time:~3,2%
set backup_dir=backups\backup_%timestamp%

:: Create backup directory
mkdir "%backup_dir%"

:: Copy folders and files
xcopy /E /I /Y engine "%backup_dir%\engine"
xcopy /E /I /Y www "%backup_dir%\www"

:: ✅ Fix: use simple copy for single files like geeth.db
if exist geeth.db copy /Y geeth.db "%backup_dir%\geeth.db"

:: ✅ Wildcards work only if files exist — so check before copying
for %%f in (*.py) do (
    copy /Y "%%f" "%backup_dir%\"
)
if exist requirements.txt copy /Y requirements.txt "%backup_dir%\"

:: Done
echo ✅ Backup completed at %timestamp%
pause
