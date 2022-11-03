
## Para criar um novo projeto
na pasta atual, usar ., para criar uma nova pasta, tirar o .
django-admin startproject <nome> .

## para iniciar um novo app
django-admin startapp <nome>

## para iniciar o server
python manage.py runserver

## criar migrations (alterações das classes que afetam o banco)
python manage.py makemigrations

## executa as  migrations
python manage.py migrate

## cria um usuário
python manage.py createsuperuser

## copia os arquivos estáticos (css, js) para produção
python manage.py collectstatic