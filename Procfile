release: python manage.py migrate
web: gunicorn dicussion_app.wsgi --log-file - && conda install -c conda-forge poppler