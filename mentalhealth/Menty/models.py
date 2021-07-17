from django.db import models

# Create your models here.

# Models are used to create database
# Each class represents one database

class Url(models.Model):
    # two tables inside this database
    link = models.CharField(max_length=1000)
    uuid = models.CharField(max_length=10)


# python manage.py makemigrations
# python manage.py migrates
# python manage.py createsuperuser
# admin
# admin@gmail.com
# localhost/admin