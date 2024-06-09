#!/bin/bash

python3 -m venv /venv

source /venv/bin/activate
pip install -r requirements.txt
pip install gunicorn

gunicorn -b 0.0.0.0:8000 main:app

deactivate
