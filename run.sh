#!/bin/bash
source /venv/bin/activate

script_dir=$(dirname "$(readlink -f "$0")")
cd websiteroute

gunicorn -b 0.0.0.0:${PORT} --chdir $script_dir main:app

deactivate