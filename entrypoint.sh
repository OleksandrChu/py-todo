#!/bin/sh


echo "Waiting for postgres..."
while ! nc -z $SQL_HOST $SQL_PORT; do
  sleep 1
done

echo "PostgreSQL started"

python manage.py migrate

exec "$@"