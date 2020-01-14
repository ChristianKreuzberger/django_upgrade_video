FROM python:3.6.10-slim-stretch
MAINTAINER ckreuzberger@localhost

COPY ./app /app

WORKDIR /app

RUN pip install --no-cache-dir -r requirements/dev.txt

COPY ./docker/dev/python/entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
