#!/bin/bash
if [[ $ENV == 'local' ]]; then
    #statements
    python manage.py migrate --noinput
    python manage.py loaddata moove_apps/fixtures/*.json
    python manage.py runserver 0.0.0.0:8000
else
   #run production docker
   python manage.py migrate --noinput
   python manage.py loaddata moove_apps/fixtures/*.json
   python manage.py collectstatic --noinput
   cp /usr/src/app/supervisor.conf /etc/supervisor/conf.d/
   cp /usr/src/app/nginx.conf /etc/nginx/conf.d/default.conf
   supervisord -n
fi
