#!/bin/bash
sudo ufw allow 8000
python3 -m venv /venv

source /venv/bin/activate
pip install -r requirements.txt
pip install gunicorn



script_dir=$(dirname "$(readlink -f "$0")")
cd websiteroute

gunicorn -b 0.0.0.0:8000 --chdir $script_dir main:app

deactivate