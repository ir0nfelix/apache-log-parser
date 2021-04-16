#!/bin/sh
. ./env.sh

python /django_application/manage.py migrate
python /django_application/manage.py collectstatic

exec gunicorn -c /django_application/gunicorn.py core.wsgi
