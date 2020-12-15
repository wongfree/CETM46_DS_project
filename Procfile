release: python manage.py migrate
release: python manage.py collectstatic
release: python -m spacy download en
release: python -m spacy link en_core_web_sm en
release: sh ~/task.sh
web: gunicorn freechatbot.wsgi --log-file -