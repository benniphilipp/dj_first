## Erstelle virtualenv
```
python3 -m venv env
```
## virtualenv Aktivren
```
. env/bin/activate
```
## Install Django Aktuelle Version
```
pip3 install Django
```
## Oder Definierte Django Version
```
pip3 install Django==2.2
```
## Django Projekt erstellen
```
django-admin startproject src
```
## Erstelle eine Django App
```
python manage.py startapp {{APP-NAME}}
```
## Django Starten
```
python manage.py runserver
```
## Datenbank migrieren
```
python3 manage.py makemigrations && python manage.py migrate
```
## Django static files erstellen
```
python manage.py collectstatic
```
## Erstelle requirements.txt
```
pip freeze > requirements.txt
```
##Bonus

## Crispy forms
```
pip install django-crispy-forms
```
## Bilder Upload
```
pip install pillow
```
