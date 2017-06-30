import platform
import os

so = platform.system().lower()

if so == 'windows':
    os.system('C:/Python35/python.exe manage.py makemigrations servicos')
    os.system('C:/Python35/python.exe manage.py makemigrations loja')

    os.system('C:/Python35/python.exe manage.py migrate servicos')
    os.system('C:/Python35/python.exe manage.py migrate loja')
    os.system('C:/Python35/python.exe manage.py migrate')

    os.system('C:/Python35/python.exe manage.py runserver')

elif so == 'linux':
    os.system('python3 manage.py makemigrations servicos')
    os.system('python3 manage.py makemigrations loja')

    os.system('python3 manage.py migrate servicos')
    os.system('python3 manage.py migrate loja')
    os.system('python3 manage.py migrate')

    os.system('python3 manage.py runserver')
else:
    print("Sistema Operacional não identificado, inicie manualmente")

