release: python manage.py migrate
web: gunicorn dicussion_app.wsgi --log-file -
RUN apt-get update && apt-get -y install poppler-utils && apt-get clean
