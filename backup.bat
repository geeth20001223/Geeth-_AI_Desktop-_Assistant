@echo off
set timestamp=%date:~10,4%-%date:~4,2%-%date:~7,2%_%time:~0,2%-%time:~3,2%
set backup_dir=backups\backup_%timestamp%
mkdir %backup_dir%

xcopy /E /I /Y engine %backup_dir%\engine
xcopy /E /I /Y www %backup_dir%\www
xcopy /I /Y geeth.db %backup_dir%\geeth.db
xcopy /I /Y *.py %backup_dir%\
xcopy /I /Y requirements.txt %backup_dir%\
echo ✅ Backup completed at %timestamp%
pause
