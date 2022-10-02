@echo off 

call %~dp0tg_bot\.venv\Scripts\activate

cd %~dp0tg_bot

set TOKEN=5795211939:AAGo98IaGS4ze6pyPtETk2w9ojj_MxSDyF0

python bot_telegram.py

pause