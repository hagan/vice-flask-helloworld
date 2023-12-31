# Dockerfile.vice_python_base
# src: https://github.com/docker-library/python/blob/35d09c044857f7aef2bf24791027f3e3fe2c34dd/3.11/alpine3.18/Dockerfile
FROM python:3.11.6-alpine3.18
# ARG BASE_IMAGE_NAME='vice_python_base'
# ARG BASE_TAG='0.0.1'
ARG BASE_DOCKER_DIR='.'
# RUN echo "BASE_DOCKER_IMAGE=${BASE_IMAGE_NAME}:${BASE_TAG}" > .env
# RUN echo "BASE_IMAGE_NAME=$BASE_IMAGE_NAME" >> .env
# RUN echo "BASE_TAG=${BASE_TAG}" >> .env
# RUN echo "BASE_DIR=${BASE_DOCKER_DIR}" >> .env

# build-essential(debian) / alpine-sdk(alpine)
RUN apk update \
    && apk add --no-cache \
        util-linux \
        openrc \
        bash \
        nginx \
        rsyslog \
        python3-dev \
        curl \
        vim \
        alpine-sdk \ 
        procps

# Create a directory to store PID files and run directories
# RUN rc-update add rsyslog default \
#   &&  mkdir /run/openrc \
#   && touch /run/openrc/softlevel

# Set up OpenRC
RUN rc-update add devfs default
RUN rc-update add nginx default
RUN rc-update add rsyslog default
RUN mkdir /run/openrc && touch /run/openrc/softlevel

COPY ${BASE_DOCKER_DIR}/entrypoint.sh /usr/local/bin/
RUN chmod u+x,g+x /usr/local/bin/entrypoint.sh \
  && ln -s /usr/local/bin/entrypoint.sh / # backwards compat

# setup gunicorn
RUN mkdir /run/gunicorn-helloworld
RUN mkdir /var/www/static
RUN mkdir /usr/src/helloworld

COPY ${BASE_DOCKER_DIR}/nginx/proxy_params /etc/nginx/proxy_params
COPY ${BASE_DOCKER_DIR}/nginx/http.d/default.conf  /etc/nginx/http.d/default.conf
COPY ${BASE_DOCKER_DIR}/gunicorn/gunicorn-helloworld.conf.py /etc/gunicorn/helloworld.conf.py
COPY ${BASE_DOCKER_DIR}/gunicorn/helloworld_app.py /usr/src/helloworld/app.py
COPY ${BASE_DOCKER_DIR}/gunicorn/gunicorn-helloworld /etc/init.d/gunicorn-helloworld

RUN chmod u+x,g+x /etc/init.d/gunicorn-helloworld && rc-update add gunicorn-helloworld default

WORKDIR /usr/src/helloworld

EXPOSE 80

COPY ${BASE_DOCKER_DIR}/requirements-base.txt ./
RUN pip install --no-cache-dir -r requirements-base.txt

RUN apk update && apk upgrade

# COPY . .

# CMD [ "python", "./your-daemon-or-script.py" ]

CMD [ "openrc", "default" ]

# CMD bash
## A neat trick to keep this docker instance running..
# CMD tail -f /dev/null

ENTRYPOINT [ "entrypoint.sh" ]