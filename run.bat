@echo off
setlocal

REM Get the current directory of the batch file
set "SCRIPT_DIR=%~dp0"

REM Set the log file path
set "LOG_FILE=%SCRIPT_DIR%\log.txt"

REM Change to the script directory
cd /d "%SCRIPT_DIR%"

REM Create and activate the main virtual environment
python -m venv venv
call venv\Scripts\activate

REM Install the remaining dependencies from requirements.txt
python -m pip install -r requirements.txt 2>> "%LOG_FILE%"

cd model_code

python API.py 2>> "%LOG_FILE%"

cd ..

REM Deactivate the virtual environment
deactivate

REM Display message and prompt user to exit
echo.
echo Batch file execution completed. Press any key to exit.
pause >nul

endlocal
