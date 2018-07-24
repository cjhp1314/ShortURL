#!/bin/sh

cd /data/server/pyenv/shortUrl/webapps/
gunicorn_conf="`pwd`/conf/gunicorn.py"
gunicorn deploy:app_wsgi -c $gunicorn_conf -D
