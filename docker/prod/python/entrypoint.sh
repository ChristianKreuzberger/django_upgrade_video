#!/bin/bash

python manage.py collectstatic --noinput

echo "Running command '$*'"
exec /bin/bash -c "$*"
