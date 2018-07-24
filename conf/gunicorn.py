workers = 4
bind = 'unix:/tmp/shorturl.sock'
proc_name = 'shorturl'
pidfile = '/tmp/shorturl.pid'
user = 'www'
group = 'www'
errorlog = '/data/server/pyenv/shortUrl/webapps/logs/gunicorn_error.log'
