release: python manage.py migrate
release: python manage.py collectstatic
release: python -m spacy download en
worker: bundle exec bash ~/task.sh
web: gunicorn freechatbot.wsgi --log-file -
