#!/bin/bash
echo "Please input the port the website will run on: "
read port

sudo ufw allow ${port}
python3 -m venv /venv

source /venv/bin/activate
pip install -r requirements.txt
pip install gunicorn
deactivate

./create_service.sh

systemctl start tunneling