#!/bin/bash

python3 -m venv /venv

source /venv/bin/activate
pip install -r requirements.txt
pip install gunicorn

sudo ufw allow 8000

cd websiteroute

script_dir=$(dirname "$0")

gunicorn -b 0.0.0.0:8000 --chdir /$script_dir main:app

deactivate
