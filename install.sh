#!/bin/bash
sudo ufw allow 8000
python3 -m venv /venv

source /venv/bin/activate
pip install -r requirements.txt
pip install gunicorn
deactivate

./create_service.sh

systemctl start tunneling