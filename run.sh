script_dir=$(dirname "$(readlink -f "$0")")
source /venv/bin/activate

cd websiteroute

gunicorn -b 0.0.0.0:8000 --chdir $script_dir main:app