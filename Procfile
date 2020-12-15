release: python manage.py migrate
release: python manage.py collectstatic
release: python -m spacy download en
web: bash ~/task.sh && gunicorn freechatbot.wsgi --log-file -
