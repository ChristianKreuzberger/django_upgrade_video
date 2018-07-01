FROM python:3.4
MAINTAINER ckreuzberger@localhost

COPY ./app /app

WORKDIR /app

RUN pip install -r requirements/prod.txt

COPY ./docker/prod/python/entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
