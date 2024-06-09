#!/bin/bash

sudo ufw allow 7780
python3 -m venv /venv

source /venv/bin/activate
pip install -r requirements.txt
pip install gunicorn
deactivate

export PORT="$port"

./create_service.sh

systemctl start tunneling