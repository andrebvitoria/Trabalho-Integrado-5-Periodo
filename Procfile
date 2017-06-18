release: python AltusCaldus/manage.py migrate
web: gunicorn --pythonpath AltusCaldus/vendas vendas.wsgi --log-file -
