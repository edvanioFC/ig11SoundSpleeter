
@echo off

REM Update pip
python -m pip install --upgrade pip

REM Create a virtual environment
python -m venv env

REM Activate the virtual environment
call env\Scripts\activate

REM Install the required packages
pip install flask==1.1.4
pip install click==8.1.3
pip install numpy==1.18.5
pip install spleeter
pip install typer==0.4.0
pip install click==7.1.2
pip install werkzeug==1.0.1
pip install jinja2==2.11.3
pip install markupsafe==2.0.1

REM Deactivate the virtual environment
deactivate

echo Setup complete. To activate the virtual environment, run "env\Scripts\activate"