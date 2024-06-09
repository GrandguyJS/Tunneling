#!/bin/bash
source /venv/bin/activate

script_dir=$(dirname "$(readlink -f "$0")")
cd websiteroute

gunicorn -b 0.0.0.0:7780 --chdir $script_dir main:app

deactivate