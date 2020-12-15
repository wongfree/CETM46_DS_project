release: python manage.py migrate
release: python manage.py collectstatic
release: python -m spacy download en
release: ./task.sh
web: gunicorn freechatbot.wsgi --log-file -