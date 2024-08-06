#!/bin/bash

# Update the package list and install prerequisites
sudo apt-get update
sudo apt-get install -y software-properties-common

# Add the deadsnakes PPA (Python 3.8)
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update

# Install Python 3.8
sudo apt-get install -y python3.8 python3.8-venv python3.8-dev

# Create a virtual environment
python3.8 -m venv env

# Activate the virtual environment
source env/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install the required packages
pip install --upgrade pip
pip install flask==1.1.4
pip install click==8.1.3
pip install numpy==1.18.5
pip install spleeter
pip install typer==0.4.0
pip install click==7.1.2
pip install werkzeug==1.0.1
pip install jinja2==2.11.3
pip install markupsafe==2.0.1


# Deactivate the virtual environment
deactivate

echo "Setup complete. To activate the virtual environment, run 'source env/bin/activate'"
