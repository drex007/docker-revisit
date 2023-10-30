#!/bin/sh

set -e #Cancels the running of scripts incase of any error

python manage.py collectstatic --noinput #Collecting static files

uwsgi --socket:8000 --master --enable-threads --module service.wsgi  #starts @ port 8000
 