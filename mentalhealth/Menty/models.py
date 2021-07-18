from django.db import models

# Create your models here.
class leaderboard(models.Model):
    name = models.CharField(max_length=100)
    score = models.CharField(max_length=100)
    

    def __str__(self) -> str:
        return self.title




























# Models are used to create database
# Each class represents one database

class Task(models.Model):
    # two tables inside this database
    task_id = models.CharField(max_length=10)
    task_title = models.CharField(max_length=1000)
    task_des = models.CharField(max_length=1000)


# python manage.py makemigrations
# python manage.py migrates
# python manage.py createsuperuser
# admin
# admin@gmail.com
# localhost/admin