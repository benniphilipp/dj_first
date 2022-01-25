# 1.Erstelle virtualenv

python3 -m venv env

# 2.virtualenv Aktivren

. env/bin/activate

# 3.Install Django Aktuelle Version

pip3 install Django

# 3.1Oder Definierte Django Version

pip3 install Django==2.2

# 4.Django Projekt erstellen

django-admin startproject src

# 5.Erstelle eine Django App

python manage.py startapp {{APP-NAME}}

# 6.Django Starten

python manage.py runserver

# 7.Datenbank migrieren

python3 manage.py makemigrations && python manage.py migrate

# 8.Django static files erstellen

python manage.py collectstatic

# 9.Erstelle requirements.txt

pip freeze > requirements.txt

##Bonus

#Crispy forms

pip install django-crispy-forms

#Bilder Upload

pip install pillow
