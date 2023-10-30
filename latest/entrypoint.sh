#!/bin/sh
set -e

echo "Service 'All': Status"

rc-status -a

# echo "Service 'RSyslog': Starting ..."

# rc-service rsyslog start

echo "Service 'Nginx': Starting..."



if [ "$1" = 'httpd' ]; then
  echo "Command: '$@'"
  echo "Service '$1': Launching ..."
  exec $@
else
  rc-service nginx start
  rc-service gunicorn-helloworld start
  # exec tail -f /dev/null
fi
