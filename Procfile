release: python manage.py migrate
release: python manage.py collectstatic
web: python -m spacy download en
web: gunicorn freechatbot.wsgi --log-file -