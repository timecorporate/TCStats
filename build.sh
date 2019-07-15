#!/bin/sh
set -e # stops execution on error
#flake8
python manage.py migrate
python manage.py test
