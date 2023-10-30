# -*- encoding: utf-8 -*-
"""
Gunicorn configuration
"""

import os
import multiprocessing

## INI VERSION:
# [program:web]
# directory = /app/that/has/www-data/permissions
# environment = APP_SETTINGS="flask_app.app.config.ProductionConfig"
# command = /app/venv/bin/gunicorn flask_app.wsgi:app \
#   -b localhost:8080 \
#   --workers 3 --worker-class gevent \
#   --keep-alive 10 \
#   --log-level info \
#   --access-logfile /app/logs/admin.gunicorn.access.log \
#   --error-logfile /app/logs/admin.gunicorn.error.log \
#   --access-logformat '%%({X-REAL-IP}i)s %%(l)s %%(u)s %%(t)s "%%(r)s" %%(s)s %%(b)s "%%(f)s" "%%(a)s"'
# user = www-data
# autostart=true
# autorestart=true


# create local environment values out of any envprefixed wit GUNICORN_

for k,v in os.environ.items():
    if k.startswith("GUNICORN_"):
        key = k.split('_', 1)[1].lower()
        print(f"GUNICORN {key} = {v}")
        locals()[key] = v

if not 'bind' in locals():
    # bind = "0.0.0.0:8080"
    bind = "unix:/run/gunicorn-helloworld/default.sock"

#spew = False if not 'spew' in locals() else (spew in ['true', 'True']))

forwarded_allowed_ips = "*" if not 'forwarded_allowed_ips' in locals() else "127.0.0.1"

worker_class = "gthread"
# worker_class = "sync"
if not 'workers' in locals():
    # workers = 4
    workers = 2

calc_workers = multiprocessing.cpu_count() * 2 + 1
print(f"if using standard equation for workers (cpu*2+1), we would have used {calc_workers}")

threads = 3

worker_tmp_dir = "/dev/shm"

umask = 0o007
# reload = True

access_log_format = '"%({X-REAL-IP}i)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
# syslog = True
# syslog_prefix = 'helloworld:'
accesslog = "-"
errorlog = "-"