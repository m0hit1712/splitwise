from django.db import models


class User(models.Model):
    email = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=12)





