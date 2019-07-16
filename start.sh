#!/bin/sh
set -e # stops execution on error
python manage.py migrate
gunicorn tcstats_api.wsgi --bind 0.0.0.0:8000 --workers 3