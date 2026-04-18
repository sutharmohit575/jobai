web: python manage.py migrate --noinput && python manage.py collectstatic --noinput && python load_demo_data.py && gunicorn jobai.wsgi:application --bind 0.0.0.0:$PORT
