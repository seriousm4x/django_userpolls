#!/usr/bin/env sh

# DB migration
python -u manage.py makemigrations
python -u manage.py migrate
python -u manage.py collectstatic --noinput

# Create superuser if none exists
python -u manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('$DJANGO_SUPERUSER_USER', password='$DJANGO_SUPERUSER_PASSWORD') if not User.objects.filter(username='$DJANGO_SUPERUSER_USER').exists() else print('Django superuser exists')"

# run gunicorn server
gunicorn polls_project.wsgi:application --bind 0.0.0.0:8000 --workers $(($(nproc) + 1)) &

# fetch emotes ever hour
while :; do
    python -u manage.py fetchEmotes
    sleep $(( 1 * 60 * 60 ))
done